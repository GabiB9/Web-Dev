import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product: any;
  @Output() liked = new EventEmitter<any>();
  @Output() removed = new EventEmitter<any>();

  likeProduct() {
    this.product.likes++;
    this.liked.emit(this.product);
  }

  removeProduct() {
    this.removed.emit(this.product);
  }
}
