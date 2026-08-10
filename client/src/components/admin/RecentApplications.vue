<script setup>
defineProps({
  applications: {
    type: Array,
    default: () => []
  }
});

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-GB', {
    day: '2-digit',
    month: 'short',
    year: 'numeric'
  });
};
</script>

<template>
  <section class="portal-card p-3 mb-4">
    <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Recent Student Applications</h2>
    <div class="table-responsive">
      <table class="table table-sm mb-0" style="font-size: 14px">
        <thead>
          <tr>
            <th>Sr.</th>
            <th>Name</th>
            <th>Drive</th>
            <th>Company</th>
            <th>Date</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(app, index) in applications" :key="app.id">
            <td>{{ index + 1 }}</td>
            <td>{{ app.studentName }}</td>
            <td>{{ app.jobTitle }}</td>
            <td>{{ app.companyName }}</td>
            <td>{{ formatDate(app.appliedAt) }}</td>
            <td>
              <router-link
                :to="`/review/${app.id}`"
                class="portal-btn portal-btn-primary py-1 px-2"
              >
                View
              </router-link>
            </td>
          </tr>
          <tr v-if="applications.length === 0">
            <td colspan="6" class="text-center text-muted py-3">
              No recent student applications.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>