<script setup>
import AdminDashboard from '@/views/admin/AdminDashboard.vue';
import StudentDashboard from '@/views/student/StudentDashboard.vue';
import CompanyDashboard from '@/views/company/CompanyDashboard.vue';

const role = localStorage.getItem('role');
</script>

<template>
  <div>
    <AdminDashboard v-if="role === 'admin' || role === 'sudo'" />
    <CompanyDashboard v-else-if="role === 'company'" />
    <StudentDashboard v-else-if="role === 'student'" />
  </div>
</template>
