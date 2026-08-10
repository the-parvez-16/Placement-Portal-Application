<script setup>
import { ref, onMounted, watch } from 'vue';
import { navbarState } from '@/store';
import Pagination from '@/components/Pagination.vue';
import api from '@/services/api';
import { useRoute } from "vue-router";

const route = useRoute();

const students = ref([
    { id: 101, name: 'CutieBoy-kun', status: 'APPROVED' }
]);
const currentPage = ref(1);
const totalPages = ref(3);


onMounted(() => {
    navbarState.value = {
        title: 'Manage Students',
        showSearch: true,
        searchPlaceholder: 'Search student name...',
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
        
        const response = await api.get(`/admin/students?page=${page}&q=${query}`);
        
        students.value = response.data.students;
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
                    <th>Student Name</th>
                    <th>Branch</th>
                    <th>CGPA</th>
                    <th>Status</th>
                    <th class="text-end">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="student in students" :key="student.id">
                    <td class="align-middle">{{ student.id }}</td>
                    <td class="align-middle fw-semibold">{{ student.name }}</td>
                    <td class="align-middle">{{ student.branch }}</td>
                    <td class="align-middle fw-bold">{{ student.cgpa }}</td>
                    <td class="align-middle">
                        <span :class="{'text-success': student.status === 'approved', 'text-warning': student.status === 'pending', 'text-danger': student.status === 'blocked'}">
                        {{ student.status }}
                    </span>
                    </td>
                    <td class="text-end">
                        <div class="d-flex gap-2 justify-content-end">
                            <router-link :to="`/user/${student.id}`" class="portal-btn portal-btn-dark mb-0">View</router-link>
                            <button v-if="student.status === 'approved'" @click="changeStatus(student.id, 'blocked')" class="portal-btn portal-btn-danger mb-0">Block</button>
                            <button v-if="student.status === 'blocked'" @click="changeStatus(student.id, 'approved')" class="portal-btn portal-btn-success mb-0">Unblock</button>
                            <template v-if="student.status !== 'approved' && student.status !== 'blocked'">
                                <button @click="changeStatus(student.id, 'approved')" class="portal-btn portal-btn-success mb-0">Approve</button>
                                <button @click="changeStatus(student.id, 'blocked')" class="portal-btn portal-btn-danger mb-0">Block</button>
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