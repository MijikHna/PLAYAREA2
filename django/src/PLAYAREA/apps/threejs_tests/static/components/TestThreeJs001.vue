<template>
  <div class="scene" ref="scene"></div>
</template>

<script>
import * as THREE from "three";

export default {
  name: "TestThreeJs001",
  data: function () {
    return {
      camera: new THREE.PerspectiveCamera(
        75,
        //el.clientWidth / el.clientHeight,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
      ),
      renderer: new THREE.WebGLRenderer({ antialias: true }),
      scene: new THREE.Scene(),
    };
  },
  mounted() {
    const navHeight = $("nav").outerHeight();

    const el = this.$refs.scene;

    // Camera
    this.camera.position.z = 5;

    // Renderer
    // this.renderer.setSize(el.clientWidht, el.clientHight);
    this.renderer.setSize(window.innerWidth, window.innerHeight - navHeight);

    el.append(this.renderer.domElement);

    // Figures
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({
      color: 0x00ff00,
    });
    const cube = new THREE.Mesh(geometry, material);

    this.scene.add(cube);

    // Animation
    const animate = () => {
      requestAnimationFrame(animate);

      cube.rotation.x += 0.01;
      cube.rotation.y += 0.01;

      this.renderer.render(this.scene, this.camera);
    };

    animate();
  },
};
</script>

<style scoped>
.scene {
  width: 100%;
  height: 100%;
}
</style>