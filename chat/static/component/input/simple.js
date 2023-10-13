class SimpleInput extends HTMLElement {
    static observedAttributes = [ "text"]
    static get observedAttributes() {
  
      return [  "text"]
    }
      constructor() {
        super();
        // element created
        this._text
      this.f
      }
    //https://flowbite.com/docs/components/card/
      connectedCallback() {
        // browser calls this method when the element is added to the document
        // (can be called many times if an element is repeatedly added/removed)
  //      this.style.color = "red";
      
      this.f = document.createElement('div')

      var label = document.createElement('label')
      label.className = "mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
      label.value = "Search"
      label.for="default-search"
        var deva = document.createElement('div')
        deva.className = "relative"
        deva.style.cssText = "top:-25px"
        deva.innerHTML = `<div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
        </svg>
    </div>
    `
    var input = document.createElement('input')
    input.id = "txt"
    input.type = "search"
    input.className ="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    input.placeholder = "Chat with me"
/*
    this.f.innerHTML = `
        
        <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
        <div class="relative" style="top:-25px">
            <div  class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
            </div>
            <input type="search" id="text" class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Chat with meeee" required>
        </div>
    `
  */ 
    this.f.appendChild(label)
    this.f.appendChild(deva)
    this.appendChild(input)
    
    this.appendChild(this.f)  


      }
      
    

    
      disconnectedCallback() {
        // browser calls this method when the element is removed from the document
        // (can be called many times if an element is repeatedly added/removed)
      }
    
      static get observedAttributes() {
        return [/* array of attribute names to monitor for changes */];
      }
    
      attributeChangedCallback(name, oldValue, newValue) {
        if(name == "text" && oldValue != null)
        {
        this._text.value  = newValue
        }
      // called when one of attributes listed above is modified
    }
    
      adoptedCallback() {
        // called when the element is moved to a new document
        // (happens in document.adoptNode, very rarely used)
      }
    
      // there can be other element methods and properties
    }
  
    customElements.define('simple-input', SimpleInput);
  
          