<script setup>
</script>
<template>
  <div class="container">
    <div class="row align-items-center">
      
      <div class="col-md-6 text-start pe-md-5">
        <h1 class="fw-bolder display-4 mb-3" style="color:var(--text-main)">
          Land Your <span style="color: var(--primary)">Dream Job</span> Today.
        </h1>
        
        <p class="fs-5 mb-4" style="color: var(--text-muted)">
          Streamlining campus placements for Institutes, Companies, and Students. 
          Apply for jobs, track your status, and kickstart your career!
        </p>
        
        <div class="d-flex gap-3">
          <router-link to="/register" class="portal-btn portal-btn-primary px-4 py-2" style="font-size: 16px;">
            Get Started <VsxIcon iconName="ArrowRight2" type="linear" size="18" class="ms-1" />
          </router-link>
          <router-link to="/login" class="portal-btn portal-btn-dark px-4 py-2" style="font-size: 16px;">
            Sign In
          </router-link>
        </div>
      </div>

      <div class="col-md-6 mt-5 mt-md-0">
        <img src="@/assets/hero.png" alt="Placement Hero" class="img-fluid w-100 drop-shadow" />
      </div>

    </div>
  </div>
</template>
