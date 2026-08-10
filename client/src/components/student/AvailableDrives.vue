<script setup>
defineProps({
  drives: {
    type: Array,
    default: () => []
  }
});
</script>

<template>
  <section class="portal-card p-3 mb-4">
      <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Available Drives</h2>

      <template v-if="drives.length > 0">
          <div v-for="drive in drives" :key="drive.id" class="portal-list-row d-flex flex-wrap justify-content-between align-items-center gap-2 py-2">
              <div>
                  <span class="fw-semibold">{{ drive.job_title }}</span>
                  <span class="text-muted ms-2" style="font-size:13px;">{{ drive.company_name }}</span>
              </div>
              <router-link :to="`/drive/${drive.id}`" class="portal-btn portal-btn-dark">
                  View Details
              </router-link>
          </div>
      </template>
      <p v-else class="text-muted mb-0">No drives available right now.</p>
  </section>
</template>