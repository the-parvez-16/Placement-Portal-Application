<script setup>
defineProps({
  companies: {
    type: Array,
    default: () => []
  }
});
</script>

<template>
  <section class="portal-card p-3 mb-4">
      <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Organizations</h2>

      <template v-if="companies.length > 0">
          <div v-for="company in companies" :key="company.id" class="portal-list-row d-flex justify-content-between align-items-center py-2">
              <span>{{ company.name }}</span>
              <router-link :to="`/company/${company.id}`" class="portal-btn portal-btn-dark">
                  View Details
              </router-link>
          </div>
      </template>
      <p v-else class="text-muted mb-0">No organizations available.</p>
  </section>
</template>