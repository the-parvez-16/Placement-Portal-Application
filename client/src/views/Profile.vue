<script setup>
import StudentProfile from '@/views/student/StudentProfile.vue';
import CompanyProfile from '@/views/company/CompanyProfile.vue';

const role = localStorage.getItem('role');
</script>

<template>
  <div>
    <CompanyProfile v-if="role === 'company'" />
    <StudentProfile v-else-if="role === 'student'" />
  </div>
</template>
