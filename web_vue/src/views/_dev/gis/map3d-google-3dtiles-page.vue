//cesiumMap.vue
<template>
  <div class="main">
    <div id="cesiumContainer" class="cesiumContainer"></div>
  </div>
</template>
<script setup lang="ts">
// vue
import { onBeforeUnmount, onMounted } from 'vue'

// 简易3d地图 cesium
import * as Cesium from 'cesium'

onMounted(() => {
  initMap()
  // 全局
  window.$ObjLargeTemp.set('viewer', viewer)
})

onBeforeUnmount(() => {
  viewer && viewer.destroy()
  window.$ObjLargeTemp.delete('viewer')
})

let viewer: Cesium.Viewer
const initMap = async () => {
  viewer = new Cesium.Viewer('cesiumContainer', {
    timeline: false,
    animation: false,
    sceneModePicker: false,
    baseLayerPicker: false
  })

  // The globe does not need to be displayed,
  // since the Photorealistic 3D Tiles include terrain
  viewer.scene.globe.show = false

  // Add Photorealistic 3D Tiles
  try {
    const tileset = await Cesium.createGooglePhotorealistic3DTileset()
    viewer.scene.primitives.add(tileset)
  } catch (error) {
    console.log(`Error loading Photorealistic 3D Tiles tileset.
  ${error}`)
  }

  // Point the camera at the Googleplex
  viewer.scene.camera.setView({
    destination: new Cesium.Cartesian3(-2693797.551060477, -4297135.517094725, 3854700.7470414364),
    orientation: new Cesium.HeadingPitchRoll(
      4.6550106925119925,
      -0.2863894863138836,
      1.3561760425773173e-7
    )
  })
}
</script>

<style scoped>
.main {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-color: blanchedalmond;
}
.cesiumContainer {
  width: 100%;
  height: 100%;
  z-index: 9999;
}
</style>
