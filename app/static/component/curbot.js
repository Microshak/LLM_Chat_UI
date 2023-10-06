class CurBot extends HTMLElement {
  static observedAttributes = [ "title", 'img','description','tags']
  static get observedAttributes() {

    return [  "title", 'img' ,'description','tags']
  }
    constructor() {
      super();
      // element created
      this._title
      this._img
      this._description
      this._tags
    }
  //https://flowbite.com/docs/components/card/
    connectedCallback() {
      // browser calls this method when the element is added to the document
      // (can be called many times if an element is repeatedly added/removed)
//      this.style.color = "red";
      let imgUrl;
      if (this.hasAttribute("img")) {
        imgUrl = this.getAttribute("img");
      } else {
        imgUrl = "img/default.png";
      }


      /*
      this.innerHTML = `<div class="card">
      <img src="${imgUrl}" alt="Avatar" style="width:110px">
      <div class="container">
        <h4><b>John Doe</b></h4>
        <p>Architect & Engineer</p>
      </div>
    </div>`
    */
    var el = document.createElement('div')
    el.className=""
    el.style.cssText="margin:20px"
    var imaa = document.createElement('a')
    imaa.href="#"
    imaa.className="float-left"
    this._img = document.createElement('img')
    this._img.src = imgUrl;
    this._img.style.cssText="width:200px;"
    var elbottom = document.createElement('div')
    elbottom.className="mx-5 "
    elbottom.style.cssText="width:60%;"
    this._title = document.createElement('h5')
    this._title.className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
    this._title.innerHTML = this.getAttribute("title")  
    var tags = this.getAttribute("tags")
    var tag = tags.split(",")
    this._tags = document.createElement('div')
    
    if(tag.includes('QA'))
    {
      this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.076-4.076a1.526 1.526 0 011.037-.443 48.282 48.282 0 005.68-.494c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
      </svg></div>`
    }
    if(tag.includes('convo'))
    {
      this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
      </svg></div>`
    }
    if(tag.includes('data'))
    {
      this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
      </svg></div>`
    }
    if(tag.includes('marketing'))
    {
      this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
      </svg>
      </div>`
    }



    this._description = document.createElement("p")
    this._description.className="mb-3 font-normal text-gray-700 dark:text-gray-400"
    this._description.innerHTML = this.getAttribute("description")
   
    this.append(el)
    
    
    imaa.appendChild(this._img)
    el.appendChild(imaa)

    
    elbottom.appendChild(this._title)
    elbottom.appendChild(this._tags)
    elbottom.appendChild(this._description)
    
    el.appendChild(elbottom)

    }
  
    disconnectedCallback() {
      // browser calls this method when the element is removed from the document
      // (can be called many times if an element is repeatedly added/removed)
    }
  
    static get observedAttributes() {
      return [/* array of attribute names to monitor for changes */];
    }
  
    attributeChangedCallback(name, oldValue, newValue) {
      if(name == "title" && oldValue != null)
      {
      this._title.innerHTML  = newValue
      }
      if(name == "img" && oldValue != null)
      {
      this._img.src  = newValue
      }
      if(name == "description" && oldValue != null)
      {
      this._description.innerHTML  = newValue
      }
      if(name == "tags" && oldValue != null)
      {
        this._tags.innerHTML = ""
        var tag = newValue.split(",")
       console.log(tag) 
        if(tag.includes('QA'))
        {
          this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.076-4.076a1.526 1.526 0 011.037-.443 48.282 48.282 0 005.68-.494c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
          </svg></div>`
        }
        if(tag.includes('convo'))
        {
          this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
          </svg></div>`
        }
        if(tag.includes('data'))
        {
          this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
          </svg></div>`
        }
        if(tag.includes('marketing'))
        {
          this._tags.innerHTML += `<div class="mt-2 flex items-center text-sm text-gray-500 ">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
          </svg>
          </div>`
        }
    
    
      }
    // called when one of attributes listed above is modified
  }
  
    adoptedCallback() {
      // called when the element is moved to a new document
      // (happens in document.adoptNode, very rarely used)
    }
  
    // there can be other element methods and properties
  }

  customElements.define('curbot-element', CurBot);

        