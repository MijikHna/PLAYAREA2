class myFeature {
  myProperty;

  constructor(settings) {
    this.myProperty = 'hello';
    this.settings = settings;
  }

  myMethod() {
    console.log(this.myProperty);
  }

  readSettings() {
    console.log(this.settings);
  }
}

class Collapsible {
  constructor(elem, numberItems = 2) {
    this.numberItems = numberItems;
    this.state = { closed: true };

    this.elem = document.querySelector(elem);

    if (!this.elem) {
      return;
    }

    this.listItems = this.elem.querySelectorAll('li');
    this.showMoreLink = this.elem.querySelector('.show-more-link');

    this.listItems.forEach((item, index) => {
      if (index < this.numberItems) {
        item.classList.add('default');
      }
    });

    this.elem.addEventListener('click', (event) => {
      if (!event.target.matches('.show-more-link')) {
        return;
      }
      this.state.closed === true
        ? (this.state.closed = false)
        : (this.state.closed = true);

      this.elem.classList.toggle('open');
      this.elem.classList.toggle('closed');

      this.render();
    });
  }

  render() {
    this.state.closed
      ? (this.showMoreLink.textContent = 'show more')
      : (this.showMoreLink.textContent = 'show less');
  }

  destroy() {
    this.elem.parentNode.removeChild(this.elem);
  }
}

$(document).ready(() => {
  const collapsibleList1 = new Collapsible('#list1');
  collapsibleList1.render();
  const collapsibleList2 = new Collapsible('#list2');
});
