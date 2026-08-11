<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { navbarState, authState } from '@/store';
import Pagination from '@/components/Pagination.vue';
import api from '@/services/api';
import { useRoute } from "vue-router";
import { formatDate } from '@/utils/formatters';

const route = useRoute();

const isCompany = computed(() => authState.value.role === 'company');
const applications = ref([
    { 
        id: "",
        student_name: "",
        drive_title: "",
        applied_at: "",
        status: "" 
    }
]);

const currentPage = ref(1);
const totalPages = ref(10);

onMounted(() => {
    navbarState.value = {
        title: 'Applications',
        showSearch: true,
        searchPlaceholder: 'Search applications...',
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
        
        const response = await api.get(`${baseUrl}/applications?page=${page}&q=${query}`);
        
        applications.value = response.data.applications;
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
                    <th>Student Name</th>
                    <th>Drive</th>
                    <th>Applied Date</th>
                    <th>Status</th>
                    <th class="text-end">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="app in applications" :key="app.id">
                    <td class="align-middle">{{ app.id }}</td>
                    <td class="align-middle fw-semibold">{{ app.student_name }}</td>
                    <td class="align-middle">{{ app.drive_title }}</td>
                    <td class="align-middle">{{ formatDate(app.applied_at) }}</td>
                    <td class="align-middle text-capitalize">{{ app.status }}</td>
                    <td class="text-end">
                        <!-- Company review karti hai, Admin dono kar sakta hai -->
                        <router-link :to="`/review/${app.id}`" class="portal-btn portal-btn-dark mb-0">
                            {{ isCompany ? 'Review' : 'View' }}
                        </router-link>
                    </td>
                </tr>
            </tbody>
        </table>
      </div>
      <Pagination :currentPage="currentPage" :totalPages="totalPages" @changePage="loadData" />
    </section>
  </div>
</template>