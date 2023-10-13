class LargeText extends HTMLElement {
    static observedAttributes = [ "text"]
    static get observedAttributes() {
  
      return [  "text", "placeholder"]
    }
      constructor() {
        super();
        // element created
        this._text
        this._placeholder 
      this.f
      }
    //https://flowbite.com/docs/components/card/
      connectedCallback() {
        // browser calls this method when the element is added to the document
        // (can be called many times if an element is repeatedly added/removed)
  //      this.style.color = "red";
      
      this.f = document.createElement('div')

      var label = document.createElement('label')
      label.className = "block mb-2 text-sm font-medium text-gray-900 dark:text-white"
      label.value = "Search"
      label.for="txt"
        
    var input = document.createElement('textarea')
    input.id = "txt"
    input.className ="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    input.rows = 12
    var placeholder = this.getAttribute("placeholder")
    
    input.setAttribute("placeholder", placeholder)
    var button = document.createElement("button")
    button.type="submit" 
//    button.form="form" 
    button.innerHTML="Submit"
    button.className = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    /*
<label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your message</label>
<textarea id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Write your thoughts here..."></textarea>    `
  */ 
    this.f.appendChild(label)
 
    this.appendChild(input)
    this.appendChild(button)
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
        console.log(name)
        if(name == "text" && oldValue != null)
        {
        this._text.value  = newValue
        }
        if(name == "placeholder" && oldValue != null)
        {
        this._placeholder  = newValue
        }
      // called when one of attributes listed above is modified
    }
    
      adoptedCallback() {
        // called when the element is moved to a new document
        // (happens in document.adoptNode, very rarely used)
      }
    
      // there can be other element methods and properties
    }
  
    customElements.define('large-input', LargeText);
  
          