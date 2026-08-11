<script setup>
import { ref } from 'vue';
import { formatDate } from '@/utils/formatters';
import api from '@/services/api';
import { alertState } from '@/store'; // Used to show notifications

defineProps({
  applications: {
    type: Array,
    default: () => []
  }
});

const isExporting = ref(false);

const handleExport = async () => {
    try {
        isExporting.value = true;
        const response = await api.post("/student/export");
        const taskId = response.data.task_id;
        
        alertState.value = { type: "info", message: "Export started! Generating CSV..." };

        const interval = setInterval(async () => {
            const statusRes = await api.get(`/student/export-status/${taskId}`);
            
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
  <section class="portal-card p-3 mb-4">
      <div class="d-flex justify-content-between align-items-center border-bottom border-dark pb-2 mb-3">
          <h2 class="fs-6 fw-bold mb-0">Applied Drives</h2>
          <button @click="handleExport" class="portal-btn portal-btn-primary" :disabled="isExporting" style="height:32px; padding: 0 15px;">
                <template v-if="isExporting">
                    <VsxIcon iconName="Timer" :size="20" type="linear" />
                    <span>Exporting...</span>
                </template>
                <template v-else>
                    <VsxIcon iconName="DocumentDownload" :size="20" type="linear" />
                    <span>Export CSV</span>
                </template>
            </button>
      </div>

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