/** Reject withdrawals that breach minimum balance (modernized from MINBAL.cbl). */

import java.math.BigDecimal;
import java.math.RoundingMode;

public final class minbal {

    private minbal() {}

    public enum StatusCode {
        OK(0),
        BELOW_MINIMUM(9);

        private final int code;

        StatusCode(int code) {
            this.code = code;
        }

        public int code() {
            return code;
        }
    }

    public record WithdrawalStatus(StatusCode code, String text) {}

    public record WithdrawalResult(
            BigDecimal balance,
            BigDecimal withdraw,
            BigDecimal remaining,
            BigDecimal minRemaining,
            WithdrawalStatus status) {}

    private static BigDecimal quantize(BigDecimal value) {
        return value.setScale(2, RoundingMode.HALF_UP);
    }

    public static WithdrawalResult evaluateWithdrawal(
            BigDecimal balance, BigDecimal withdraw, BigDecimal minRemaining) {
        BigDecimal remaining = quantize(balance.subtract(withdraw));
        WithdrawalStatus status =
                remaining.compareTo(minRemaining) < 0
                        ? new WithdrawalStatus(StatusCode.BELOW_MINIMUM, "BELOW MINIMUM")
                        : new WithdrawalStatus(StatusCode.OK, "OK");
        return new WithdrawalResult(
                quantize(balance), quantize(withdraw), remaining, quantize(minRemaining), status);
    }

    public static void main(String[] args) {
        WithdrawalResult result =
                evaluateWithdrawal(
                        new BigDecimal("1200.00"),
                        new BigDecimal("950.00"),
                        new BigDecimal("500.00"));

        System.out.println("MINBAL START");
        System.out.println("BALANCE=" + result.balance().toPlainString());
        System.out.println("WITHDRAW=" + result.withdraw().toPlainString());
        System.out.println("REMAIN=" + result.remaining().toPlainString());
        if (result.status().code() == StatusCode.BELOW_MINIMUM) {
            System.out.println("REJECTED=" + result.status().text());
        } else {
            System.out.println("APPROVED=" + result.status().text());
        }
        System.out.println("MINBAL END");
    }
}
