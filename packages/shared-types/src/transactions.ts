export interface Transaction {
  id: string;
  merchantId: string;
  orderId: string;
  amount: number;
  currency: string;
  cardBrand: string;
  cardLastFour: string;
  customerEmail: string;
  status: string;
  createdAt: string;
}

export type ChargebackStatus =
  | "detected"
  | "analyzing"
  | "disputing"
  | "resolved_won"
  | "resolved_lost"
  | "expired";

export interface Chargeback {
  id: string;
  transactionId: string;
  merchantId: string;
  reasonCode: string;
  amount: number;
  currency: string;
  cardBrand: string;
  status: ChargebackStatus;
  deadline: string;
  detectedAt: string;
}
