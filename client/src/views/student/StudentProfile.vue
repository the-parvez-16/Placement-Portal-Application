<script setup>
import { ref, onMounted } from 'vue';
import { navbarState } from '@/store';

// Yeh data tumhare backend API se aayega
const studentData = ref({
    name: 'Demon16', 
    email: 'student@example.com',
    education: '',
    skills: '',
    resume_link: ''
});

onMounted(() => {
    // Header ko automatically setup kar dega back button ke sath
    navbarState.value = {
        title: 'Edit Profile',
        showSearch: false,
        showProfileBtn: false,
        showBackBtn: true,
        backRoute: '/dashboard' 
    };
});

const saveChanges = async () => {
    console.log("Saving student profile...", studentData.value);
    // Yahan Axios ke through backend API call jayegi
    // Response aane par toast/alert trigger kar dena
};
</script>

<template>
  <div class="row justify-content-center w-100">
      <div class="col-12 col-lg-8">
          <section class="portal-card p-4 mb-4 mt-2">

              <div class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
                  <div>
                      <h2 class="fs-4 fw-bold mb-1">{{ studentData.name }}</h2>
                      <span class="fs-6 fw-bold text-muted">{{ studentData.email }}</span>
                  </div>
                  <span class="portal-btn portal-btn-dark" style="pointer-events: none;">
                      Role: Student
                  </span>
              </div>

              <form @submit.prevent="saveChanges">
                  
                  <div class="mb-3">
                      <strong class="d-block mb-2">Education History</strong>
                      <textarea v-model="studentData.education" class="form-control portal-search-input w-100" 
                                style="height: 80px; border-radius: 5px; font-size: 14px;" 
                                placeholder="e.g. B.Tech Computer Science (2022-2026), CGPA: 8.5"></textarea>
                  </div>

                  <div class="mb-3">
                      <strong class="d-block mb-2">Technical & Soft Skills</strong>
                      <textarea v-model="studentData.skills" class="form-control portal-search-input w-100" 
                                style="height: 80px; border-radius: 5px; font-size: 14px;" 
                                placeholder="e.g. Python, Flask, C, Cyber Security"></textarea>
                  </div>

                  <div class="mb-4">
                      <strong class="d-block mb-2">Resume Link (Google Drive / GitHub)</strong>
                      <input type="url" v-model="studentData.resume_link" class="form-control portal-search-input w-100" 
                             style="font-size: 14px;"
                             placeholder="https://...">
                      <small class="text-muted d-block mt-1" style="font-size: 13px;">Please ensure the link is set to "Anyone with the link can view".</small>
                  </div>

                  <div class="d-flex gap-2 border-top border-dark pt-3 mt-4 justify-content-end">
                      <button type="submit" class="portal-btn portal-btn-primary">Save Changes</button>
                  </div>

              </form>

          </section>
      </div>
  </div>
</template>