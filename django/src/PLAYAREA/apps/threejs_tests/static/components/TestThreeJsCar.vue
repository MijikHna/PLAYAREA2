<template>
  <div ref="scene"></div>
</template>

<script>
import * as THREE from "three";
import TestThreeJs001Vue from "./TestThreeJs001.vue";

export default {
  name: "TestThreeJsCar",
  data() {
    return {
      // Scene
      scene: new THREE.Scene(),
      // Light
      //ambient light scheint von allen Richtugnen = gibt die Base-Color
      ambientLight: new THREE.AmbientLight(0xffffff, 0.6), //Color und Intensity (0-1.0) des Lichts sitzen
      // dirctianl Light schient von weitem mit parallelen Linien wie Sonnne
      directinalLicht: new THREE.DirectionalLight(0x00ff00, 0.8),

      //Camera (Perspective z.B Videospiele (mehr zu sehen in der Ferne), Orthographic = ein Rechteck)
      // 75 Units (nicht Pixel) weg vom Kegelstumpf
      camera: new THREE.OrthographicCamera(
        150 / -2, //left
        150 / 2, //right
        150 / (window.innerWidth / window.innerHeight) / 2, //top
        150 / (window.innerWidth / window.innerHeight) / -2, //bottom
        0, //near plane
        1000 // far plane
      ),

      //Render
      renderer: new THREE.WebGLRenderer({ antialias: true }),
    };
  },
  mounted() {
    const el = this.$refs.scene;
    el.appendChild(this.renderer.domElement);

    const navHeight = $("nav").outerHeight();

    // Light
    this.scene.add(this.ambientLight);

    this.directinalLicht.position.set(200, 500, 300); // position relativ zu 0,0,0 setzen. Die genauen Werte sind nicht so wichtig eher die deren Proportionen
    this.scene.add(this.directinalLicht);

    // Camera
    // 200 Units in jeder Richtung bewegen
    this.camera.position.set(200, 200, 200);
    // Camera auf 0,10,0 schauen lassen
    this.camera.lookAt(0, 10, 0);

    // Renderer
    this.renderer.setSize(window.innerWidth, window.innerHeight - navHeight);

    const car = this.creatCar();
    this.scene.add(car);

    this.renderer.render(this.scene, this.camera);

    /*
    const animate = () => {
      requestAnimationFrame(animate);

      car.rotation.x += 0.01;
      car.rotation.y += 0.01;

      this.renderer.render(this.scene, this.camera);
    };
    animate();
    */
  },
  methods: {
    createWheel() {
      const geometry = new THREE.BoxBufferGeometry(12, 12, 33); // x, y ,z
      // alternative Materialen: MeshBasicMaterial, MeshLambertMaterial, MeshPhongMaterial
      const material = new THREE.MeshLambertMaterial({
        color: 0x333333,
      });

      const wheel = new THREE.Mesh(geometry, material);

      return wheel;
    },
    creatCar() {
      const car = new THREE.Group();

      const backWheel = this.createWheel();
      backWheel.position.y = 6;
      backWheel.position.x = -18;

      const frontWheel = this.createWheel();
      frontWheel.position.y = 6;
      frontWheel.position.x = 18;

      const mainCar = new THREE.Mesh(
        new THREE.BoxBufferGeometry(60, 15, 30),
        new THREE.MeshLambertMaterial({ color: 0xa52523 })
      );
      mainCar.position.y = 12;

      // Texturen für jede Seite erstellen
      const carFrontTexture = this.getCarFrontTexture();
      const carBackTexture = this.getCarFrontTexture();
      const carRightSideTexture = this.getCarSideTexture();
      const carLeftSideTexture = this.getCarSideTexture();
      carLeftSideTexture.center = new THREE.Vector2(0.5, 0.5);
      carLeftSideTexture.rotation = Math.PI;
      carLeftSideTexture.flipY = false;

      const cabin = new THREE.Mesh(
        // new THREE.BoxBufferGeometry(33, 12, 24),
        // new THREE.MeshLambertMaterial({ color: 0xffffff }),

        new THREE.BoxBufferGeometry(33, 12, 24),
        [
          new THREE.MeshLambertMaterial({ map: carFrontTexture }),
          new THREE.MeshLambertMaterial({ map: carBackTexture }),
          new THREE.MeshLambertMaterial({ color: 0xffffff }), // top
          new THREE.MeshLambertMaterial({ color: 0xffffff }), // bottom
          new THREE.MeshLambertMaterial({ map: carRightSideTexture }),
          new THREE.MeshLambertMaterial({ map: carLeftSideTexture }),
        ]
      );
      cabin.position.x = -6;
      cabin.position.y = 25.5;

      car.add(backWheel);
      car.add(frontWheel);
      car.add(mainCar);
      car.add(cabin);

      return car;
    },
    getCarFrontTexture() {
      const canvas = document.createElement("canvas");
      canvas.winth = 64;
      canvas.height = 32;
      const context = canvas.getContext("2d");

      // ganzes Canvas mit Weiß füllen
      context.fillStyle = "#ffffff";
      context.fillRect(0, 0, 64, 32);
      // zweite (kleineren) Rechnteck mit grau füllen
      context.fillStyle = "#666666";
      context.fillRect(8, 8, 48, 24);

      return new THREE.CanvasTexture(canvas);
    },
    getCarSideTexture() {
      const canvas = document.createElement("canvas");
      canvas.winth = 128;
      canvas.height = 32;
      const context = canvas.getContext("2d");

      context.fillStyle = "#ffffff";
      context.fillRect(0, 0, 128, 32);
      context.fillStyle = "#666666";
      context.fillRect(10, 8, 38, 24);
      context.fillRect(58, 8, 60, 24);

      return new THREE.CanvasTexture(canvas);
    },
  },
};
</script>

<style></style>