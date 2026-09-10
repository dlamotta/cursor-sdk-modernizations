/** Monthly maintenance fee on low-balance accounts (modernized from FEECALC.cbl). */

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;
import java.util.Locale;

public final class feecalc {

    private feecalc() {}

    public record FeeResult(
            BigDecimal balance,
            BigDecimal minBalance,
            BigDecimal fee,
            BigDecimal newBalance,
            boolean feeApplied) {}

    private static BigDecimal quantize(BigDecimal value) {
        return value.setScale(2, RoundingMode.HALF_UP);
    }

    public static FeeResult calculateFee(
            BigDecimal balance, BigDecimal minBalance, BigDecimal fee) {
        if (balance.compareTo(minBalance) < 0) {
            BigDecimal newBalance = quantize(balance.subtract(fee));
            return new FeeResult(balance, minBalance, fee, newBalance, true);
        }
        return new FeeResult(balance, minBalance, fee, balance, false);
    }

    public static String formatCurrency(BigDecimal amount) {
        return NumberFormat.getCurrencyInstance(Locale.US).format(amount);
    }

    public static void main(String[] args) {
        FeeResult result =
                calculateFee(
                        new BigDecimal("450.75"),
                        new BigDecimal("500.00"),
                        new BigDecimal("12.50"));

        System.out.println("FEECALC START");
        System.out.println("BALANCE=" + result.balance());
        System.out.println("MIN=" + result.minBalance());
        if (result.feeApplied()) {
            System.out.println("FEE APPLIED=" + result.fee());
            System.out.println("NEW BALANCE=" + formatCurrency(result.newBalance()));
        } else {
            System.out.println("NO FEE");
        }
        System.out.println("FEECALC END");
    }
}
