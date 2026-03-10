export type DisputeStatus =
  | "pending"
  | "evidence_gathering"
  | "submitted"
  | "under_review"
  | "won"
  | "lost";

export interface Dispute {
  id: string;
  chargebackId: string;
  merchantId: string;
  status: DisputeStatus;
  reasonCode: string;
  amount: number;
  currency: string;
  createdAt: string;
  updatedAt: string;
}
