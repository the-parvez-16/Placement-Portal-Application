<script setup>
import { formatDate } from '@/utils/formatters';

defineProps({
  applications: {
    type: Array,
    default: () => []
  }
});
</script>

<template>
  <section class="portal-card p-3 mb-4">
      <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Applied Drives</h2>

      <div class="table-responsive">
          <table class="table table-sm mb-0" style="font-size:14px;">
              <thead>
                  <tr>
                      <th>Sr.</th>
                      <th>Drive Name</th>
                      <th>Company</th>
                      <th>Date</th>
                      <th>Status</th>
                      <th>Action</th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="(app, index) in applications" :key="app.id">
                      <td>{{ index + 1 }}</td>
                      <td>{{ app.drive_title }}</td>
                      <td>{{ app.company_name }}</td>
                      <td>{{ formatDate(app.applied_at) }}</td>
                      <td>
                          <span class="badge bg-secondary text-white text-capitalize">
                              {{ app.status }}
                          </span>
                      </td>
                      <td>
                          <router-link :to="`/drive/${app.drive_id}`" class="portal-btn portal-btn-primary">
                              View Details
                          </router-link>
                      </td>
                  </tr>
                  <tr v-if="applications.length === 0">
                      <td colspan="6" class="text-center text-muted py-3">No drives applied yet.</td>
                  </tr>
              </tbody>
          </table>
      </div>
  </section>
</template>