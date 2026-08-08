<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const role = localStorage.getItem('role');
const dashboardData = ref({
  total_students: 0,
  total_companies: 0,
  total_drives: 0,
  total_apps: 0,
  pending_companies: [],
  pending_drives: []
});

onMounted(async () => {
  try {
    const token = localStorage.getItem("access_token");
    const response = await axios.get("/admin/dashboard", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });
    
    dashboardData.value = response.data;
  } catch (error) {
    console.error("Failed to load dashboard data!", error);
  }
});
</script>

<template>
  <h1>{{  role.charAt(0).toUpperCase() + role.slice(1) }} Dashboard</h1>
  <!-- Paste your body HTML here! -->
  <div class="container py-3 d-flex flex-column min-vh-100">
    <!-- Replace Jinja variables with Vue variables -->
    <h3 class="fs-2 fw-bold mb-0">{{ dashboardData.total_students }}</h3>
    
    <!-- Replace Jinja loops {% for %} with Vue v-for -->
    <!-- <div v-for="company in dashboardData.pending_companies" :key="company.id"> ... </div> -->
  </div>
</template>