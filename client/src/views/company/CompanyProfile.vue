<script setup>
import { ref, onMounted } from "vue";
import { navbarState, alertState } from "@/store";
import api from "@/services/api";

const companyData = ref({
  name: "",
  email: "",
  location: "",
  industry: "",
  about: "",
  hr_contact: "",
  website: "",
});

onMounted( async () => {
    navbarState.value = {
        title: "Company Profile",
        showSearch: false,
        showProfileBtn: false,
        showBackBtn: true,
        backRoute: "/dashboard",
    };

    try{
        const response = await api.get("/company/profile");
        companyData.value = response.data;
    }catch(err) {
        let errorMsg = err.response?.data?.error || "Failed to load company profile.";
    
        if (typeof errorMsg === 'object') {
            const firstField = Object.keys(errorMsg)[0];
            const specificError = errorMsg[firstField][0];
            const capitalizedField = firstField.charAt(0).toUpperCase() + firstField.slice(1);
            errorMsg = `${capitalizedField}: ${specificError}`;
        }
        alertState.value = {
            type: "danger",
            message: errorMsg
        };
    }
});

const saveChanges = async () => {
    try {
        const response = await api.put("/company/profile", companyData.value);
        companyData.value = response.data.profile;
        alertState.value = {
            type: "success",
            message: response.data.message || "Profile updated successfully!",
        };
    } catch (err) {
        let errorMsg = err.response?.data?.error || "Failed to update profile.";

        if (typeof errorMsg === 'object') {
            const firstField = Object.keys(errorMsg)[0];
            const specificError = errorMsg[firstField][0];
            const capitalizedField = firstField.charAt(0).toUpperCase() + firstField.slice(1);
            errorMsg = `${capitalizedField}: ${specificError}`;
        }
        alertState.value = {
        type: "danger",
        message: errorMsg
        };
    }
};
</script>

<template>
  <div class="row justify-content-center w-100">
    <div class="col-12 col-lg-8">
      <section class="portal-card p-4 mb-4 mt-2">
        <div
          class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3"
        >
          <div>
            <h2 class="fs-4 fw-bold mb-1">{{ companyData.name }}</h2>
            <span class="fs-6 fw-bold text-muted">{{ companyData.email }}</span>
          </div>
          <span class="portal-btn portal-btn-dark" style="pointer-events: none">
            Role: Organization
          </span>
        </div>

        <form @submit.prevent="saveChanges">
          <div class="mb-3">
            <strong class="d-block mb-2">Organization Name *</strong>
            <input
              type="text"
              v-model="companyData.name"
              class="form-control portal-search-input w-100"
              style="font-size: 14px"
              required
            />
          </div>

          <div class="mb-3">
            <strong class="d-block mb-2">Location *</strong>
            <input
              type="text"
              v-model="companyData.location"
              class="form-control portal-search-input w-100"
              style="font-size: 14px"
              required
            />
          </div>

          <div class="mb-3">
            <strong class="d-block mb-2">Industry *</strong>
            <input
              type="text"
              v-model="companyData.industry"
              class="form-control portal-search-input w-100"
              style="font-size: 14px"
              required
            />
          </div>

          <div class="mb-3">
            <strong class="d-block mb-2">About the Company *</strong>
            <textarea
              v-model="companyData.about"
              class="form-control portal-search-input w-100"
              style="font-size: 14px; min-height: 100px"
              required
            ></textarea>
          </div>

          <div class="mb-3">
            <strong class="d-block mb-2">HR Contact *</strong>
            <input
              type="text"
              v-model="companyData.hr_contact"
              class="form-control portal-search-input w-100"
              style="font-size: 14px"
              placeholder="e.g. 9876543210"
              required
              minlength="10"
              maxlength="10"
            />
          </div>

          <div class="mb-4">
            <strong class="d-block mb-2">Company Website *</strong>
            <input
              type="url"
              v-model="companyData.website"
              class="form-control portal-search-input w-100"
              style="font-size: 14px"
              placeholder="https://..."
              required
            />
          </div>

          <div
            class="d-flex gap-2 border-top border-dark pt-3 mt-4 justify-content-end"
          >
            <button type="submit" class="portal-btn portal-btn-primary">
              Save Changes
            </button>
          </div>
        </form>
      </section>
    </div>
  </div>
</template>
