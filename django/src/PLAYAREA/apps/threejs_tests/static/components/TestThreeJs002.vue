<template>
  <div class="scene" ref="scene"></div>
</template>

<script>
import * as THREE from "three";

export default {
  name: "TestThreeJs002",
  data: function () {
    return {
      ambientLight: new THREE.AmbientLight(0xffffff, 0.6),
      directionalLight: new THREE.DirectionalLight(0xffffff, 0.8),
      camera: null,
      renderer: new THREE.WebGLRenderer({ antialias: true }),
      scene: new THREE.Scene(),
    };
  },
  mounted() {
    const el = this.$refs.scene;
    el.append(this.renderer.domElement);

    // Light
    this.scene.add(this.ambientLight);

    this.directionalLight.position.set(200, 500, 300);
    this.scene.add(this.directionalLight);

    // Camera
    const aspectRatio = window.innerWidth / window.innerHeight;
    const cameraWidth = 150;
    const cameraHeight = cameraWidth / aspectRatio;

    // const camera = new THREE.OrthographicCamera(
    this.camera = new THREE.OrthographicCamera(
      cameraWidth / -2, // left
      cameraWidth / 2, // right
      cameraHeight / 2, // top
      cameraHeight / -2, // bottom
      0, // near plane
      1000 // far plane
    );
    this.camera.position.set(200, 200, 200);
    this.camera.lookAt(0, 10, 0);

    // Renderer
    this.renderer.setSize(window.innerWidth, window.innerHeight);

    // Create Figures
    const wheel = this.createWheels();
    this.scene.add(wheel);

    // Animate
    const animate = () => {
      requestAnimationFrame(animate);

      wheel.rotation.x += 0.01;
      wheel.rotation.y += 0.01;

      this.renderer.render(this.scene, this.camera);
    };

    animate();
  },
  methods: {
    createWheels() {
      const geometry = new THREE.BoxBufferGeometry(12, 12, 33);
      const material = new THREE.MeshLambertMaterial({ color: 0x333333 });
      const wheel = new THREE.Mesh(geometry, material);
      return wheel;
    },
  },
};
</script>

<style scoped>
.scene {
  width: 100%;
  height: 100%;
}
</style>