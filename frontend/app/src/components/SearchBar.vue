<template>
<span class="relative w-full mr-4">
  <input type="search" placeholder="Search all notes..." class="text-grey-lighter w-full text-base transition border border-transparent focus:outline-none rounded shadow bg-grey-darker px-2 pl-8 appearance-none leading-normal ds-input">
  <div class="absolute search-icon" style="top: .2rem; left: .6rem;">
    <svg class="fill-current text-grey pointer-events-none w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
      <path d="M12.9 14.32a8 8 0 1 1 1.41-1.41l5.35 5.33-1.42 1.42-5.33-5.34zM8 14A6 6 0 1 0 8 2a6 6 0 0 0 0 12z"></path>
    </svg>
  </div>
</span>
</template>

<script>

export default {
  name: "SearchBar"
};
</script>
