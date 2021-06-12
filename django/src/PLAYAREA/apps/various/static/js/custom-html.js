/**
 * 1. Klasse erstellen, die von HTMLElement Klasse erbt
 * 2. in die Klasse connectCallback() einfügen, damit es in den DOM eingeschlossen wird
 * 3. als CustomElement registerien
 */

// 1
export class Salutation extends HTMLElement {
  // 2
  connectedCallback() {
    this.innerHTML = `<h1>Hello World...</h1>`;
    this.style.color = 'red';
  }
}
