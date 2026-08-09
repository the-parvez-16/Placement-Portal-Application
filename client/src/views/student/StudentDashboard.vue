<script setup>
import { ref, onMounted } from 'vue';
import { navbarState } from '@/store';
import OrganizationsList from '@/components/student/OrganizationsList.vue';
import AppliedDrives from '@/components/student/AppliedDrives.vue';
import AvailableDrives from '@/components/student/AvailableDrives.vue';

// Ye data backend API se fetch hoga
const studentName = ref("Student"); 
const companiesList = ref([]);
const studentApplications = ref([]);
const approvedDrivesList = ref([]);

onMounted(() => {
    // Header Setup
    navbarState.value = {
        title: `Welcome, ${studentName.value}`,
        showSearch: true,
        searchPlaceholder: 'Search role, company, skills…',
        showProfileBtn: true,
        profileRoute: '/profile', // Dynamic routing ke hisaab se
        showBackBtn: false
    };
});
</script>

<template>
  <div class="flex-grow-1 w-100">
    <div class="row g-4">
        
        <!-- Left Column -->
        <div class="col-12 col-md-6">
            <OrganizationsList :companies="companiesList" />
            <AppliedDrives :applications="studentApplications" />
        </div>

        <!-- Right Column -->
        <div class="col-12 col-md-6">
            <AvailableDrives :drives="approvedDrivesList" />
        </div>

    </div>
  </div>
</template>