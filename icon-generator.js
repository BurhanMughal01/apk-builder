/* APKForge — Icon Generator */
(function() {
  'use strict';

  const SIZES = [48, 72, 96, 144, 192, 512];
  const ADAPTIVE_SIZES = [108, 162, 216, 324, 432];

  const IconGen = {
    originalImage: null,
    croppedDataURL: null,
    bgColor: '#059669',
    fgColor: '#ffffff',

    // Load uploaded file
    async loadFile(file) {
      return new Promise((resolve, reject) => {
        if (!file || !file.type.startsWith('image/')) {
          reject(new Error('Please upload a PNG, JPG, or SVG file'));
          return;
        }
        if (file.size > 5 * 1024 * 1024) {
          reject(new Error('File too large (max 5MB)'));
          return;
        }
        const reader = new FileReader();
        reader.onload = (e) => {
          const img = new Image();
          img.onload = () => {
            this.originalImage = img;
            resolve(img);
          };
          img.onerror = () => reject(new Error('Invalid image'));
          img.src = e.target.result;
        };
        reader.onerror = () => reject(new Error('Failed to read file'));
        reader.readAsDataURL(file);
      });
    },

    // Crop image to square (center crop) and resize
    cropToSquare(size = 512) {
      if (!this.originalImage) return null;
      const img = this.originalImage;
      const minDim = Math.min(img.width, img.height);
      const sx = (img.width - minDim) / 2;
      const sy = (img.height - minDim) / 2;

      const canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      const ctx = canvas.getContext('2d');
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = 'high';
      ctx.drawImage(img, sx, sy, minDim, minDim, 0, 0, size, size);

      this.croppedDataURL = canvas.toDataURL('image/png');
      return this.croppedDataURL;
    },

    // Generate all sizes for legacy icon
    generateAll() {
      if (!this.originalImage) return null;
      const result = {};
      SIZES.forEach(size => {
        result['mipmap-' + this._densityName(size)] = this._resizeTo(size);
      });
      return result;
    },

    // Generate adaptive icon layers
    generateAdaptive() {
      if (!this.originalImage && !this.bgColor) return null;
      const result = { foreground: {}, background: this.bgColor };
      ADAPTIVE_SIZES.forEach(size => {
        result.foreground['mipmap-' + this._densityName(size)] = this._resizeTo(size, true);
      });
      return result;
    },

    // Generate from initials (no image)
    fromInitials(text, bgColor, fgColor) {
      const canvas = document.createElement('canvas');
      canvas.width = 512;
      canvas.height = 512;
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = bgColor || this.bgColor;
      ctx.fillRect(0, 0, 512, 512);
      ctx.fillStyle = fgColor || this.fgColor;
      ctx.font = 'bold 220px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      const initials = (text || '?').substring(0, 2).toUpperCase();
      ctx.fillText(initials, 256, 256);
      this.croppedDataURL = canvas.toDataURL('image/png');
      return this.croppedDataURL;
    },

    // Internal: resize to specific size
    _resizeTo(size, transparent = false) {
      if (!this.originalImage) return null;
      const img = this.originalImage;
      const minDim = Math.min(img.width, img.height);
      const sx = (img.width - minDim) / 2;
      const sy = (img.height - minDim) / 2;

      const canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      const ctx = canvas.getContext('2d');

      if (transparent) {
        // Adaptive icon foreground — image at 66% of canvas, centered
        const inner = size * 0.66;
        const offset = (size - inner) / 2;
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(img, sx, sy, minDim, minDim, offset, offset, inner, inner);
      } else {
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(img, sx, sy, minDim, minDim, 0, 0, size, size);
      }

      return canvas.toDataURL('image/png');
    },

    _densityName(size) {
      const map = {
        48: 'mdpi', 72: 'hdpi', 96: 'xhdpi', 144: 'xxhdpi', 192: 'xxxhdpi',
        108: 'mdpi', 162: 'hdpi', 216: 'xhdpi', 324: 'xxhdpi', 432: 'xxxhdpi',
        512: 'playstore'
      };
      return map[size] || size;
    },

    // Public API
    getCroppedDataURL() { return this.croppedDataURL; },
    hasImage() { return this.originalImage !== null; },
    reset() {
      this.originalImage = null;
      this.croppedDataURL = null;
    }
  };

  window.IconGen = IconGen;
})();
