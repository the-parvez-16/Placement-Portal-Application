<script setup>
import StatsCards from "@/components/admin/StatsCards.vue";
import PendingApprovals from "@/components/admin/PendingApprovals.vue";
import RecentApplications from "@/components/admin/RecentApplications.vue";
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import api from "@/services/api";
import { alertState, navbarState } from "@/store";

const route = useRoute();

const role = localStorage.getItem('role');
const stats = ref({
  totalStudents: 0,
  totalCompanies: 0,
  totalDrives: 0,
  totalApplications: 0
});

const pending = ref({
  pendingCompanies: [],
  pendingDrives: []
});

onMounted(async () => {
  navbarState.value = { 
    title: 'Welcome Admin',
    showSearch: true,
    searchPlaceholder:
    'Search student / organization…',
    showBackBtn: false 
  };

  await fetchDashboardData();
});

watch(() => route.query.q, async (newQuery) => {
  navbarState.value.searchQuery = newQuery || "";
  await fetchDashboardData(newQuery);
});

const fetchDashboardData = async (query="") => {
  try {
    const statsResponse = await api.get(`/admin/dashboard/stats?q=${query}`);
    stats.value = statsResponse.data;

    const pendingResponse = await api.get(`/admin/dashboard/pending?q=${query}`);
    pending.value = pendingResponse.data;

  } catch (err) {
    alertState.value = {
      message: err.response?.data?.error || "Failed to load dashboard data!",
      type: "danger"
    }
  }
}
</script>

<template>
  <div class="flex-grow-1">
    
    <!-- Statistics -->
    <StatsCards :data="stats" />

    <div class="row g-4">
      
      <!-- Pending -->
      <div class="col-12 col-md-6">
        <PendingApprovals 
          :pendingCompanies="pendingCompanyUsers" 
          :pendingDrives="pendingDrives"
          @approveCompany="approveCompany"
          @approveDrive="approveDrive"
        />
        
        <!-- full lists -->
        <div class="d-flex gap-2 mt-3">
            <router-link to="/admin/companies" class="portal-btn portal-btn-dark w-100 text-center">View All Companies</router-link>
            <router-link to="/admin/students" class="portal-btn portal-btn-dark w-100 text-center">View All Students</router-link>
        </div>
      </div>

      <!-- Recent Activity -->
      <div class="col-12 col-md-6">
        <RecentApplications :applications="recentApplications" />
        
        <div class="d-flex gap-2 mt-3">
            <router-link to="/admin/drives" class="portal-btn portal-btn-dark w-100 text-center">Manage All Drives</router-link>
            <router-link to="/admin/applications" class="portal-btn portal-btn-dark w-100 text-center">View All Applications</router-link>
        </div>
      </div>

    </div>
  </div>
</template>