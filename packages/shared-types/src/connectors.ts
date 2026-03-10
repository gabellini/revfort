export type ConnectorType = "payment" | "ecommerce" | "customer_service" | "card_brand";

export type ConnectorProvider =
  | "pagarme"
  | "cielo"
  | "rede"
  | "paypal"
  | "vtex"
  | "betalabs"
  | "tray"
  | "shopify"
  | "zendesk"
  | "visa"
  | "mastercard";

export interface ConnectorConfig {
  id: string;
  merchantId: string;
  type: ConnectorType;
  provider: ConnectorProvider;
  isActive: boolean;
  createdAt: string;
}
