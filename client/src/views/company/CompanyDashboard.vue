<script setup>
import { ref, onMounted } from 'vue';
import { navbarState } from '@/store';
import StatusBanner from '@/components/company/StatusBanner.vue';
import UpcomingDrives from '@/components/company/UpcomingDrives.vue';
import ClosedDrives from '@/components/company/ClosedDrives.vue';
import DriveApplications from '@/components/company/DriveApplications.vue';
import CreateDriveModal from '@/components/company/CreateDriveModal.vue';

// Test status: 'PENDING', 'APPLIED', 'APPROVED', 'BLOCKED'
const companyStatus = ref('APPROVED'); 
const upcomingDrives = ref([]);
const closedDrives = ref([]);

onMounted(() => {
    navbarState.value = {
        title: 'Company Dashboard',
        showSearch: false,
        showProfileBtn: true,
        showBackBtn: false
    };
});
</script>

<template>
  <div class="flex-grow-1 w-100">
    
    <StatusBanner v-if="companyStatus !== 'APPROVED'" :status="companyStatus" />

    <div v-else class="row g-4">
        
        <div class="col-12 col-md-6">
            <UpcomingDrives :drives="upcomingDrives" />
            <ClosedDrives :drives="closedDrives" />
        </div>

        <div class="col-12 col-md-6">
            <DriveApplications :drives="upcomingDrives" />
        </div>

    </div>

    <CreateDriveModal v-if="companyStatus === 'APPROVED'" />

  </div>
</template>