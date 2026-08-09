<script setup>
import { ref, onMounted } from 'vue';
import { navbarState } from '@/store';

// Yeh data API se fetch hoga backend se
const companyData = ref({
    name: 'Demon16 Corp', 
    email: 'contact@demon16.com',
    hr_contact: '',
    website: ''
});

onMounted(() => {
    // Header ko automatically setup kar dega back button ke sath
    navbarState.value = {
        title: 'Company Profile',
        showSearch: false,
        showProfileBtn: false,
        showBackBtn: true,
        backRoute: '/dashboard'
    };
});

const saveChanges = async () => {
    console.log("Saving changes...", companyData.value);
    // Yahan Axios ke through backend API call jayegi
    // response aane par alertState (Toast) ko update kar dena!
};
</script>

<template>
  <div class="row justify-content-center w-100">
      <div class="col-12 col-lg-8">
          <section class="portal-card p-4 mb-4 mt-2">

              <div class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
                  <div>
                      <h2 class="fs-4 fw-bold mb-1">{{ companyData.name }}</h2>
                      <span class="fs-6 fw-bold text-muted">{{ companyData.email }}</span>
                  </div>
                  <span class="portal-btn portal-btn-dark" style="pointer-events: none;">
                      Role: Organization
                  </span>
              </div>

              <form @submit.prevent="saveChanges">
                  
                  <div class="mb-3">
                      <strong class="d-block mb-2">Organization Name *</strong>
                      <input type="text" v-model="companyData.name" class="form-control portal-search-input w-100" 
                              style="font-size: 14px;" required>
                  </div>

                  <div class="mb-3">
                      <strong class="d-block mb-2">HR Contact Person / Number</strong>
                      <input type="text" v-model="companyData.hr_contact" class="form-control portal-search-input w-100" 
                              style="font-size: 14px;"
                              placeholder="e.g. Bill Gates / +1-9876543210">
                  </div>

                  <div class="mb-4">
                      <strong class="d-block mb-2">Company Website</strong>
                      <input type="url" v-model="companyData.website" class="form-control portal-search-input w-100" 
                              style="font-size: 14px;"
                              placeholder="https://...">
                  </div>

                  <div class="d-flex gap-2 border-top border-dark pt-3 mt-4 justify-content-end">
                      <button type="submit" class="portal-btn portal-btn-primary">Save Changes</button>
                  </div>

              </form>

          </section>
      </div>
  </div>
</template>