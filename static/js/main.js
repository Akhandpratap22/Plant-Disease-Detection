/**
 * main.js — PlantGuard AI Frontend Logic
 * Drag-and-drop upload, image preview, loading states, animations
 */

document.addEventListener('DOMContentLoaded', () => {

  // ─────────────────────────────────────────────────────────────────
  // Navbar scroll effect
  // ─────────────────────────────────────────────────────────────────
  const navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // ─────────────────────────────────────────────────────────────────
  // Drag-and-Drop Upload Zone
  // ─────────────────────────────────────────────────────────────────
  const dropZone      = document.getElementById('drop-zone');
  const fileInput     = document.getElementById('file-input');
  const dropContent   = document.getElementById('drop-content');
  const previewContent = document.getElementById('preview-content');
  const previewImg    = document.getElementById('preview-img');
  const previewName   = document.getElementById('preview-name');
  const previewSize   = document.getElementById('preview-size');
  const removeBtn     = document.getElementById('remove-preview');
  const submitBtn     = document.getElementById('submit-btn');
  const uploadForm    = document.getElementById('upload-form');
  const loadingState  = document.getElementById('loading-state');

  if (!dropZone) return; // Not on upload page

  // Prevent default drag behaviors
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(event => {
    dropZone.addEventListener(event, e => {
      e.preventDefault();
      e.stopPropagation();
    });
  });

  // Drag enter/over — highlight
  ['dragenter', 'dragover'].forEach(event => {
    dropZone.addEventListener(event, () => {
      dropZone.classList.add('drag-over');
    });
  });

  // Drag leave/drop — remove highlight
  ['dragleave', 'drop'].forEach(event => {
    dropZone.addEventListener(event, () => {
      dropZone.classList.remove('drag-over');
    });
  });

  // Handle file drop
  dropZone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileSelect(files[0]);
    }
  });

  // Click on drop zone (but not on file input itself)
  dropZone.addEventListener('click', (e) => {
    if (e.target === removeBtn || removeBtn.contains(e.target)) return;
    fileInput.click();
  });

  // File input change
  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      handleFileSelect(fileInput.files[0]);
    }
  });

  // Remove preview
  if (removeBtn) {
    removeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      clearPreview();
    });
  }

  function handleFileSelect(file) {
    // Validate type
    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp', 'image/bmp'];
    if (!allowedTypes.includes(file.type)) {
      showToast('❌ Invalid file type. Please upload JPG, PNG, WEBP, or BMP.', 'error');
      return;
    }

    // Validate size (16 MB)
    if (file.size > 16 * 1024 * 1024) {
      showToast('❌ File too large. Maximum size is 16 MB.', 'error');
      return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
      previewImg.src = e.target.result;
      previewImg.alt = file.name;
      previewName.textContent = file.name;
      previewSize.textContent = formatFileSize(file.size);

      dropContent.style.display = 'none';
      previewContent.style.display = 'flex';
      submitBtn.disabled = false;
      submitBtn.classList.add('ready');

      // Update drop zone style
      dropZone.style.borderStyle = 'solid';
      dropZone.style.borderColor = 'var(--primary)';
      dropZone.style.background = 'rgba(82, 183, 136, 0.05)';
    };
    reader.readAsDataURL(file);
  }

  function clearPreview() {
    previewContent.style.display = 'none';
    dropContent.style.display = 'flex';
    previewImg.src = '';
    fileInput.value = '';
    submitBtn.disabled = true;
    submitBtn.classList.remove('ready');

    // Reset drop zone style
    dropZone.style.borderStyle = 'dashed';
    dropZone.style.borderColor = '';
    dropZone.style.background = '';
  }

  function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  }

  // ─────────────────────────────────────────────────────────────────
  // Form Submit with Loading Animation
  // ─────────────────────────────────────────────────────────────────
  if (uploadForm) {
    uploadForm.addEventListener('submit', (e) => {
      if (!fileInput.files.length) {
        e.preventDefault();
        showToast('Please select a leaf image first.', 'error');
        return;
      }

      // Show loading state
      dropZone.style.display = 'none';
      if (loadingState) {
        loadingState.style.display = 'flex';
        animateLoadingSteps();
      }
      submitBtn.disabled = true;
      submitBtn.innerHTML = `
        <div class="spinner-ring" style="width:20px;height:20px;border-width:2px;"></div>
        <span>Analyzing...</span>
      `;
    });
  }

  function animateLoadingSteps() {
    const steps = [
      document.getElementById('step-1'),
      document.getElementById('step-2'),
      document.getElementById('step-3'),
    ];
    if (!steps[0]) return;

    steps.forEach(s => s && s.classList.remove('active'));
    steps[0] && steps[0].classList.add('active');

    setTimeout(() => {
      steps[0] && steps[0].classList.remove('active');
      steps[1] && steps[1].classList.add('active');
    }, 1200);

    setTimeout(() => {
      steps[1] && steps[1].classList.remove('active');
      steps[2] && steps[2].classList.add('active');
    }, 2400);
  }

  // ─────────────────────────────────────────────────────────────────
  // Toast Notification
  // ─────────────────────────────────────────────────────────────────
  function showToast(message, type = 'info') {
    // Remove existing toasts
    document.querySelectorAll('.js-toast').forEach(t => t.remove());

    const toast = document.createElement('div');
    toast.className = `flash flash-${type} js-toast`;
    toast.style.cssText = `
      position: fixed; top: 80px; right: 24px; z-index: 3000;
      min-width: 300px; animation: slideInRight 0.3s ease;
    `;
    toast.innerHTML = `
      <span>${message}</span>
      <button onclick="this.parentElement.remove()" class="flash-close">✕</button>
    `;
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 4000);
  }

  // ─────────────────────────────────────────────────────────────────
  // Scroll reveal animations
  // ─────────────────────────────────────────────────────────────────
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe animatable elements
  const animatables = document.querySelectorAll(
    '.tip-card, .step, .crop-card, .alt-card, .info-section-card, .quick-info-panel'
  );

  animatables.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = `opacity 0.5s ease ${i * 0.05}s, transform 0.5s ease ${i * 0.05}s`;
    observer.observe(el);
  });

  // ─────────────────────────────────────────────────────────────────
  // Result Page: Animate confidence arc on load
  // ─────────────────────────────────────────────────────────────────
  const confArc = document.getElementById('conf-arc');
  if (confArc) {
    const targetDash = confArc.getAttribute('stroke-dasharray');
    confArc.setAttribute('stroke-dasharray', '0 201');
    setTimeout(() => {
      confArc.setAttribute('stroke-dasharray', targetDash);
      confArc.style.transition = 'stroke-dasharray 1.5s cubic-bezier(0.4, 0, 0.2, 1)';
    }, 300);
  }

  // Animate confidence bar on result page
  const confBar = document.getElementById('conf-bar');
  if (confBar) {
    const targetWidth = confBar.style.width;
    confBar.style.width = '0%';
    setTimeout(() => {
      confBar.style.width = targetWidth;
    }, 300);
  }

  // Animate alternative bars
  document.querySelectorAll('.alt-bar-fill').forEach((bar) => {
    const targetWidth = bar.style.width;
    bar.style.width = '0%';
    setTimeout(() => {
      bar.style.width = targetWidth;
    }, 500);
  });

  // ─────────────────────────────────────────────────────────────────
  // Smooth scroll for anchor links
  // ─────────────────────────────────────────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80; // navbar height
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ─────────────────────────────────────────────────────────────────
  // Auto-dismiss flash messages after 5 seconds
  // ─────────────────────────────────────────────────────────────────
  document.querySelectorAll('.flash').forEach(flash => {
    setTimeout(() => {
      flash.style.opacity = '0';
      flash.style.transform = 'translateX(100%)';
      flash.style.transition = '0.3s ease';
      setTimeout(() => flash.remove(), 300);
    }, 5000);
  });

});
