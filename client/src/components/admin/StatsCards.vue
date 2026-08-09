<script setup>
defineProps({
  data: {
    type: Object,
    required: true,
    default: () => ({
      totalStudents: 0,
      totalCompanies: 0,
      totalDrives: 0,
      totalApplications: 0
    })
  }
});
</script>

<template>
  <section class="row g-3 mb-4">
    <div class="col-6 col-md-3">
      <div class="portal-card p-3 text-center" style="background-color: #f8f9fa">
        <h3 class="fs-2 fw-bold mb-0">{{ data.totalStudents }}</h3>
        <span class="text-muted fw-bold" style="font-size: 13px">Total Students</span>
      </div>
    </div>
    <div class="col-6 col-md-3">
      <div class="portal-card p-3 text-center" style="background-color: #f8f9fa">
        <h3 class="fs-2 fw-bold mb-0">{{ data.totalCompanies }}</h3>
        <span class="text-muted fw-bold" style="font-size: 13px">Total Companies</span>
      </div>
    </div>
    <div class="col-6 col-md-3">
      <div class="portal-card p-3 text-center" style="background-color: #f8f9fa">
        <h3 class="fs-2 fw-bold mb-0">{{ data.totalDrives }}</h3>
        <span class="text-muted fw-bold" style="font-size: 13px">Placement Drives</span>
      </div>
    </div>
    <div class="col-6 col-md-3">
      <div class="portal-card p-3 text-center" style="background-color: #f8f9fa">
        <h3 class="fs-2 fw-bold mb-0">{{ data.totalApplications }}</h3>
        <span class="text-muted fw-bold" style="font-size: 13px">Job Applications</span>
      </div>
    </div>
  </section>
</template>