<script setup>
import { ref, onMounted, watch } from 'vue';
import { navbarState } from '@/store';
import Pagination from '@/components/Pagination.vue';
import api from '@/services/api';
import { useRoute } from "vue-router";

const route = useRoute();

const companies = ref([]);
const currentPage = ref(1);
const totalPages = ref(5);

onMounted(() => {
    navbarState.value = {
        title: 'Manage Companies',
        showSearch: true,
        searchPlaceholder: 'Search companies...',
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
        
        const response = await api.get(`/admin/companies?page=${page}&q=${query}`);
        
        companies.value = response.data.companies; 
        currentPage.value = response.data.current_page;
        totalPages.value = response.data.total_pages;
    } catch (err) {
        console.error("Error fetching data:", err);
    }
};

const changeStatus = async (id, newStatus) => {
    try {
        await api.put(`/admin/users/${id}/status`, { status: newStatus });
        loadData(currentPage.value);
    } catch (err) {
        console.error("Failed to update status", err);
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
                    <th>Organization Name</th>
                    <th>Industry</th>
                    <th>Location</th>
                    <th>Status</th>
                    <th class="text-end">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="company in companies" :key="company.id">
                    <td class="align-middle">{{ company.id }}</td>
                    <td class="align-middle fw-semibold">{{ company.name }}</td>
                    <td class="align-middle">{{ company.industry }}</td>
                    <td class="align-middle">{{ company.location }}</td>
                    <td class="align-middle">
                        <span :class="{'text-success': company.status === 'approved', 'text-warning': company.status === 'pending', 'text-danger': company.status === 'blocked'}">
                        {{ company.status }}
                    </span>

                    </td>
                    <td class="text-end">
                        <div class="d-flex gap-2 justify-content-end">
                            <router-link :to="`/user/${company.id}`" class="portal-btn portal-btn-dark mb-0">View</router-link>
                            <button v-if="company.status === 'approved'" @click="changeStatus(company.id, 'blocked')" class="portal-btn portal-btn-danger mb-0">Block</button>
                            <button v-if="company.status === 'blocked'" @click="changeStatus(company.id, 'approved')" class="portal-btn portal-btn-success mb-0">Unblock</button>
                            <template v-if="company.status !== 'approved' && company.status !== 'blocked'">
                                <button @click="changeStatus(company.id, 'approved')" class="portal-btn portal-btn-success mb-0">Approve</button>
                                <button @click="changeStatus(company.id, 'blocked')" class="portal-btn portal-btn-danger mb-0">Block</button>
                            </template>
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