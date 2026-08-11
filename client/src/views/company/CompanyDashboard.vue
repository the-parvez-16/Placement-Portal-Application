<script setup>
import { ref, onMounted } from 'vue';
import { navbarState, alertState } from '@/store';
import StatusBanner from '@/components/company/StatusBanner.vue';
import UpcomingDrives from '@/components/company/UpcomingDrives.vue';
import ClosedDrives from '@/components/company/ClosedDrives.vue';
import RejectedDrives from '@/components/company/RejectedDrives.vue';
import DriveApplications from '@/components/company/DriveApplications.vue';
import CreateDriveModal from '@/components/company/CreateDriveModal.vue';
import api from "@/services/api"

// Test status: 'PENDING', 'APPLIED', 'APPROVED', 'BLOCKED'
const companyStatus = ref(""); 
const upcomingDrives = ref([]);
const closedDrives = ref([]);
const rejectedDrives = ref([]);
const company = ref(null);

onMounted( async () => {
    try{
        const profileRes = await api.get("/company/profile");
        const drivesRes = await api.get("/company/drives");
        company.value = profileRes.data
        companyStatus.value = profileRes.data.status;
        upcomingDrives.value = drivesRes.data.filter(d => d.status === "approved" || d.status === "pending");
        closedDrives.value = drivesRes.data.filter(d => d.status === "closed");
        rejectedDrives.value = drivesRes.data.filter(d => d.status === 'rejected')
    }catch(err){
        alertState.value ={
            type: "danger",
            message: "Error fetching data"
        }
    }
    navbarState.value = {
        title: `Welcome, ${company.value.name}`,
        showSearch: false,
        showProfileBtn: true,
        showBackBtn: false
    };
});

const handleStatusUpdate = async (driveId, newStatus) => {
    try {
        await api.put(`/company/drive/${driveId}/status`, { status: newStatus });
        alertState.value = { type: 'success', message: 'Drive status updated!' };
        
        // Refresh the drive lists instantly
        const drivesRes = await api.get("/company/drives");
        upcomingDrives.value = drivesRes.data.filter(d => d.status === "approved" || d.status === "pending");
        closedDrives.value = drivesRes.data.filter(d => d.status === "closed");
    } catch (err) {
        alertState.value = { type: 'danger', message: err.response?.data?.error || 'Failed to update status' };
    }
};

</script>

<template>
  <div class="flex-grow-1 w-100">
    
    <StatusBanner v-if="companyStatus !== 'approved'" :status="companyStatus" />

    <div v-else class="row g-4">
        
        <div class="col-12 col-md-6">
            <UpcomingDrives :drives="upcomingDrives" @updateStatus="handleStatusUpdate" />
            <ClosedDrives :drives="closedDrives" @updateStatus="handleStatusUpdate" />
            <RejectedDrives :drives="rejectedDrives" @updateStatus="handleStatusUpdate" />
        </div>

        <div class="col-12 col-md-6">
            <DriveApplications :drives="upcomingDrives" />
        </div>

    </div>

    <CreateDriveModal v-if="companyStatus === 'approved'" />

  </div>
</template>