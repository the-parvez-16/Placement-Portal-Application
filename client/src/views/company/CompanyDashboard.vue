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


const isExporting = ref(false);

const handleExport = async () => {
    try {
        isExporting.value = true;
        const response = await api.post("/company/export");
        const taskId = response.data.task_id;
        
        alertState.value = { type: "info", message: "Export started! Generating CSV..." };

        const interval = setInterval(async () => {
            const statusRes = await api.get(`/company/export-status/${taskId}`);
            
            if (statusRes.data.status === 'SUCCESS') {
                clearInterval(interval);
                isExporting.value = false;
                alertState.value = { type: "success", message: "Export complete!" };
                
                window.location.href = statusRes.data.download_url;
            } else if (statusRes.data.status === 'FAILURE') {
                clearInterval(interval);
                isExporting.value = false;
                alertState.value = { type: "danger", message: "Export failed." };
            }
        }, 2000); 

    } catch(err) {
        console.log(err)
        isExporting.value = false;
        alertState.value = { type: "danger", message: "Failed to start export" };
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
            <button @click="handleExport" class="portal-btn portal-btn-primary w-100 mb-4 py-2 d-flex justify-content-center align-items-center gap-2" :disabled="isExporting">
                <template v-if="isExporting">
                    <VsxIcon iconName="Timer" :size="20" type="linear" />
                    <span> Generating CSV Please Wait...</span>
                </template>
                <template v-else>
                    <VsxIcon iconName="DocumentDownload" :size="20" type="linear" />
                    <span> Export All Applications (CSV)</span>
                </template>
            </button>
            
            <DriveApplications :drives="upcomingDrives" />
        </div>
    </div>

    <CreateDriveModal v-if="companyStatus === 'approved'" />

  </div>
</template>