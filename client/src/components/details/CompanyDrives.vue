<script setup>
defineProps({ drives: { type: Array, default: () => [] } });
</script>

<template>
  <section class="portal-card p-4">
      <h3 class="fs-5 fw-bold border-bottom border-dark pb-2 mb-3">Available Placement Drives</h3>

      <template v-if="drives && drives.length > 0">
          <div v-for="drive in drives" :key="drive.id" class="portal-list-row d-flex flex-wrap justify-content-between align-items-center gap-2 py-2 mb-2">
              <div>
                  <span class="fw-semibold d-block">{{ drive.job_title }}</span>
                  <span class="text-muted" style="font-size: 13px;">Salary: ₹{{ drive.salary || 'Not Specified' }}</span>
              </div>
              
              <router-link :to="`/drive/${drive.id}`" class="portal-btn portal-btn-primary mb-0">
                  View Details
              </router-link>
          </div>
      </template>
      <p v-else class="text-muted mb-0 fst-italic">This organization currently has no active placement drives.</p>
  </section>
</template>