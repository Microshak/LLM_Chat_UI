class Header extends HTMLElement {
    constructor() {
      super();
      // element created
    }
  //https://flowbite.com/docs/components/card/
    connectedCallback() {
      // browser calls this method when the element is added to the document
      // (can be called many times if an element is repeatedly added/removed)
//      this.style.color = "red";
      
      this.innerHTML = `
      <nav class="inset-0 z-10 block h-max w-full max-w-full rounded-none border border-white/80 bg-white bg-opacity-80 py-2 px-4 text-white shadow-md backdrop-blur-2xl backdrop-saturate-200 lg:px-8 lg:py-4">
        <div>
          <div class="container mx-auto flex items-center justify-between text-gray-900">
            <a
              href="#"
              class="mr-4 block cursor-pointer py-1.5 font-sans text-sm font-normal leading-normal text-inherit antialiased"
            >
              <span>AI BOT</span>
            </a>
            <ul class="hidden items-center gap-6 lg:flex">
              <li class="block p-1 font-sans text-sm font-normal leading-normal text-inherit antialiased">
                <a class="flex items-center" href="#">
                  Chat
                </a>
              </li>
              <li class="block p-1 font-sans text-sm font-normal leading-normal text-inherit antialiased">
                <a class="flex items-center" href="./image">
                  Image
                </a>
              </li>
              <li class="block p-1 font-sans text-sm font-normal leading-normal text-inherit antialiased">
                <a class="flex items-center" href="#">
                  Forum
                </a>
              </li>
              <li class="block p-1 font-sans text-sm font-normal leading-normal text-inherit antialiased">
                <a class="flex items-center" href="#">
                  Docs
                </a>
              </li>
            </ul>
          </div>
      </div>
    </nav>`
  
  }
  
    disconnectedCallback() {
      // browser calls this method when the element is removed from the document
      // (can be called many times if an element is repeatedly added/removed)
    }
  
    static get observedAttributes() {
      return [/* array of attribute names to monitor for changes */];
    }
  
    attributeChangedCallback(name, oldValue, newValue) {
      // called when one of attributes listed above is modified
    }
  
    adoptedCallback() {
      // called when the element is moved to a new document
      // (happens in document.adoptNode, very rarely used)
    }
  
    // there can be other element methods and properties
  }

  customElements.define('header-element', Header);

        