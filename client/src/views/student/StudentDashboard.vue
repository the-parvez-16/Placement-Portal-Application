<script setup>
import { ref, onMounted, watch } from 'vue';
import { navbarState, alertState } from '@/store';
import OrganizationsList from '@/components/student/OrganizationsList.vue';
import AppliedDrives from '@/components/student/AppliedDrives.vue';
import AvailableDrives from '@/components/student/AvailableDrives.vue';
import api from "@/services/api"
import { useRoute } from 'vue-router';

const route = useRoute();

const studentName = ref("Student"); 
const companiesList = ref([]);
const studentApplications = ref([]);
const approvedDrivesList = ref([]);

onMounted(async () => {
    try {
        const profileRes = await api.get("/student/profile");
        studentName.value = profileRes.data.name;

        const applicationRes = await api.get('/student/applications');
        studentApplications.value = applicationRes.data;

        await fetchDashboardData(route.query.q || "");
    } catch(err) {
        alertState.value = { type: "danger", message: "Failed to load drives" };
    }
    navbarState.value = {
        title: `Welcome, ${studentName.value}`,
        showSearch: true,
        searchPlaceholder: 'Search role, company, skills…',
        showProfileBtn: true,
        profileRoute: '/profile',
        showBackBtn: false
    };

});

watch(() => route.query.q, async (newQuery) => {
    await fetchDashboardData(newQuery || "");
});


const fetchDashboardData = async (searchQuery = "") => {
    try {
        const drivesRes = await api.get(`/student/drives?q=${searchQuery}`);
        approvedDrivesList.value = drivesRes.data;

        const compRes = await api.get(`/student/companies?q=${searchQuery}`);
        companiesList.value = compRes.data;
    } catch(err) {
        console.error("Failed to load dashboard data", err);
    }
}

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