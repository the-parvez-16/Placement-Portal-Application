<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { navbarState, authState } from '@/store';
import Pagination from '@/components/Pagination.vue';
import api from '@/services/api';
import { useRoute } from "vue-router";

const route = useRoute();

const isAdmin = computed(() => authState.value.role === 'admin' || authState.value.role === 'sudo');

const drives = ref([
    { id: 201, job_title: 'Frontend Developer', company_name: 'Tech Solutions', status: 'ONGOING' }
]);
const currentPage = ref(1);
const totalPages = ref(4);

onMounted(() => {
    navbarState.value = {
        title: 'Placement Drives',
        showSearch: true,
        searchPlaceholder: 'Search drives, roles...',
        showBackBtn: true,
        backRoute: '/dashboard'
    };
    loadData(1);
});

watch(() => route.query.q, () => {
    loadData(1);
});

const loadData = async (page = 1) => {
    try {
        const query = navbarState.value.searchQuery || '';
        const role = authState.value.role;
        const baseUrl = (role === 'admin' || role === 'sudo') ? '/admin' : `/${role}`;
        
        const response = await api.get(`${baseUrl}/drives?page=${page}&q=${query}`);
        
        drives.value = response.data.drives;
        currentPage.value = response.data.current_page;
        totalPages.value = response.data.total_pages;
    } catch (err) {
        console.error("Error fetching data:", err);
    }
};
</script>

<template>
  <div class="w-100">
    <section class="portal-card p-4">
      <div class="table-responsive">
        <table class="table table-sm mb-0" style="font-size:14px;">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Job Title</th>
                    <th>Company</th>
                    <th>Status</th>
                    <th class="text-end">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="drive in drives" :key="drive.id">
                    <td class="align-middle">{{ drive.id }}</td>
                    <td class="align-middle fw-semibold">{{ drive.job_title }}</td>
                    <td class="align-middle">{{ drive.company_name }}</td>
                    <td class="align-middle">{{ drive.status }}</td>
                    <td class="text-end">
                        <div class="d-flex gap-2 justify-content-end">
                            <router-link :to="`/drive/${drive.id}`" class="portal-btn portal-btn-dark mb-0">
                                View Details
                            </router-link>
                            <!-- API integration ke baad 'Manage' or 'Apply' buttons aayenge -->
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
      </div>
      <Pagination :currentPage="currentPage" :totalPages="totalPages" @changePage="loadData" />
    </section>
  </div>
</template>