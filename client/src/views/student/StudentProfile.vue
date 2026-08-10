<script setup>
import { ref, onMounted } from 'vue';
import { navbarState, alertState } from '@/store';
import api from '@/services/api';

const studentData = ref({
    email: "",
    name: "",
    branch: "",
    cgpa: "",
    expectedGraduationYear: "",
    skills: "",
    resumeFile: ""
});
const selectedFile = ref(null);

onMounted(async () => {
    navbarState.value = {
        title: "Edit Profile",
        showSearch: false,
        showProfileBtn: false,
        showBackBtn: true,
        backRoute: "/dashboard"
    };
    try {
        const response = await api.get('/student/profile');
        studentData.value = response.data;
    } catch (err) {
        alertState.value = {
            type: "danger",
            message: "Failed to fetch profile."
        };
    }
});

const handleFileUpload = (event) => {
    selectedFile.value = event.target.files[0];
};

const saveChanges = async () => {
    const formData = new FormData();
    formData.append("name", studentData.value.name);
    formData.append("branch", studentData.value.branch);
    formData.append("cgpa", studentData.value.cgpa);
    formData.append("expectedGraduationYear", studentData.value.expectedGraduationYear);
    formData.append("skills", studentData.value.skills);
    
    if (selectedFile.value) {
        formData.append("resumeFile", selectedFile.value);
    } else {
        formData.append("resumeFile", studentData.value.resumeFile);
    }

    try {
        const response = await api.put('/student/profile', formData);
        studentData.value = response.data.profile;
        selectedFile.value = null;

        alertState.value = {
            type: "success",
            message: "Profile updated successfully!"
        };

    } catch (err) {
        alertState.value = {
            type: "danger",
            message: "Failed to update profile."
        };
    }
};
</script>

<template>
  <div class="row justify-content-center w-100 m-0">
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
                    <strong class="d-block mb-2">Full Name *</strong>
                    <input type="text" v-model="studentData.name" class="form-control portal-search-input w-100" required />
                </div>

                <div class="mb-3">
                    <strong class="d-block mb-2">Branch *</strong>
                    <input type="text" v-model="studentData.branch" class="form-control portal-search-input w-100" required />
                </div>

                <div class="row">
                    <div class="col-md-6 mb-3">
                        <strong class="d-block mb-2">CGPA *</strong>
                        <input type="number" step="0.01" min="0" max="10" v-model="studentData.cgpa" class="form-control portal-search-input w-100" required />
                    </div>
                    <div class="col-md-6 mb-3">
                        <strong class="d-block mb-2">Graduation Year *</strong>
                        <input type="number" min="2020" max="2030" v-model="studentData.expectedGraduationYear" class="form-control portal-search-input w-100" required />
                    </div>
                </div>

                <div class="mb-3">
                    <strong class="d-block mb-2">Technical & Soft Skills *</strong>
                    <textarea v-model="studentData.skills" class="form-control portal-search-input w-100" placeholder="e.g. Python, Flask, Vue" required></textarea>
                </div>

               <div class="mb-4">
                    <strong class="d-block mb-2">
                        <VsxIcon iconName="DocumentUpload" :size="20" type="linear" class="me-1" />
                        Resume (PDF Only) *
                    </strong>
                    
                    <a v-if="studentData.resumeFile" :href="studentData.resumeFile" target="_blank" class="d-block mb-2 text-primary">View Current Resume</a>
                    
                    <input type="file" accept="application/pdf" @change="handleFileUpload" class="form-control portal-search-input w-100" />
                </div>


                <div class="d-flex gap-2 border-top border-dark pt-3 mt-4 justify-content-end">
                    <button type="submit" class="portal-btn portal-btn-primary">Save Changes</button>
                </div>

            </form>

          </section>
      </div>
  </div>
</template>