<script setup>
defineProps({
  pendingCompanyUsers: {
    type: Array,
    default: () => []
  },
  pendingDrives: {
    type: Array,
    default: () => []
  }
});

defineEmits(['approveCompany', 'approveDrive']);
</script>

<template>
  <div>
    <!-- Pending Company Applications -->
    <section class="portal-card p-3 mb-4">
      <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Pending Company Applications</h2>
      <template v-if="pendingCompanyUsers.length > 0">
        <div
          v-for="user in pendingCompanyUsers"
          :key="user.id"
          class="portal-list-row d-flex flex-wrap justify-content-between align-items-center gap-2 py-2"
        >
          <span>{{ user.company_name }}</span>
          <div class="d-flex gap-2 align-items-center">
            <router-link
              :to="`/user/${user.id}`"
              class="portal-btn portal-btn-dark mb-0"
            >
              View
            </router-link>
            <button
              @click="$emit('approveCompany', user.id)"
              class="portal-btn portal-btn-success mb-0"
            >
              Approve
            </button>
          </div>
        </div>
      </template>
      <p v-else class="text-muted mb-0">No pending applications.</p>
    </section>

    <!-- Pending Drives -->
    <section class="portal-card p-3 mb-4">
      <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Pending Drives</h2>
      <template v-if="pendingDrives.length > 0">
        <div
          v-for="drive in pendingDrives"
          :key="drive.id"
          class="portal-list-row d-flex flex-wrap justify-content-between align-items-center gap-2 py-2"
        >
          <span>
            <strong>{{ drive.id }}</strong> — {{ drive.job_title }} ({{ drive.company.name }})
          </span>
          <div class="d-flex gap-2">
            <router-link
              :to="`/drive/${drive.id}`"
              class="portal-btn portal-btn-dark"
            >
              View Details
            </router-link>
            <button 
              @click="$emit('approveDrive', drive.id)" 
              class="portal-btn portal-btn-success"
            >
              Approve
            </button>
          </div>
        </div>
      </template>
      <p v-else class="text-muted mb-0">No pending drives.</p>
    </section>
  </div>
</template>