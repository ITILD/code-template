<template>
  <div absolute left-0 top-0 w-full h-full ref="dropdownRef" v-if="show" :class="bg ? 'pointer-events-auto bg-op90' : 'pointer-events-none'">
    <!-- 中间 -->
    <slot pointer-events-auto></slot>
  </div>
</template>
<script setup lang="ts">
/**
 * 外部按钮优先   内部监听只负责监听非外部按钮事件且在当前组件区域外
 * 改变外部状态，点击外部自动关闭
 * 使用方法：
 * 
 * <button @click="showFun = !showFun">  Fun <button/>
 *  <SimplePopover v-model="showFun">
      <div  v-show="showFun">              
    const showFun = ref(false)
 */
defineProps(['show', 'bg'])
</script>
