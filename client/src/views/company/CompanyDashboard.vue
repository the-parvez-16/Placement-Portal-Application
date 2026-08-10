<script setup>
import { ref, onMounted } from 'vue';
import { navbarState, alertState } from '@/store';
import StatusBanner from '@/components/company/StatusBanner.vue';
import UpcomingDrives from '@/components/company/UpcomingDrives.vue';
import ClosedDrives from '@/components/company/ClosedDrives.vue';
import DriveApplications from '@/components/company/DriveApplications.vue';
import CreateDriveModal from '@/components/company/CreateDriveModal.vue';
import api from "@/services/api"

// Test status: 'PENDING', 'APPLIED', 'APPROVED', 'BLOCKED'
const companyStatus = ref(""); 
const upcomingDrives = ref([]);
const closedDrives = ref([]);

onMounted( async () => {
    navbarState.value = {
        title: 'Company Dashboard',
        showSearch: false,
        showProfileBtn: true,
        showBackBtn: false
    };
    try{
        const profileRes = await api.get("/company/profile")
        const drivesRes = await api.get("/company/drives")
        companyStatus.value = profileRes.data.status;
        upcomingDrives.value = drivesRes.data.filter(d => d.status === "approved" || d.status === "pending");
        closedDrives.value = drivesRes.data.filter(d => d.status === "closed");
    }catch(err){
        alertState.value ={
            type: "danger",
            message: "Error fetching data"
        }
    }
});
</script>

<template>
  <div class="flex-grow-1 w-100">
    
    <StatusBanner v-if="companyStatus !== 'approved'" :status="companyStatus" />

    <div v-else class="row g-4">
        
        <div class="col-12 col-md-6">
            <UpcomingDrives :drives="upcomingDrives" />
            <ClosedDrives :drives="closedDrives" />
        </div>

        <div class="col-12 col-md-6">
            <DriveApplications :drives="upcomingDrives" />
        </div>

    </div>

    <CreateDriveModal v-if="companyStatus === 'approved'" />

  </div>
</template>