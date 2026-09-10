/** Savings interest for a statement period (modernized from INTCALC.cbl). */

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;
import java.util.Locale;

public final class intcalc {

    private static final BigDecimal DAYS_PER_YEAR = new BigDecimal("365");
    /** 5.25%; legacy PIC 9V99 truncated to 0.05. */
    private static final BigDecimal DEFAULT_ANNUAL_RATE = new BigDecimal("0.0525");

    private intcalc() {}

    public record InterestResult(
            BigDecimal principal,
            BigDecimal annualRate,
            int days,
            BigDecimal dailyRate,
            BigDecimal dailyInterest,
            BigDecimal totalInterest,
            BigDecimal newBalance) {}

    private static BigDecimal quantize(BigDecimal value) {
        return value.setScale(2, RoundingMode.HALF_UP);
    }

    public static BigDecimal calcDailyRate(BigDecimal annualRate) {
        return annualRate.divide(DAYS_PER_YEAR, 10, RoundingMode.HALF_UP);
    }

    public static BigDecimal calcDailyInterest(BigDecimal principal, BigDecimal dailyRate) {
        return quantize(principal.multiply(dailyRate));
    }

    public static BigDecimal accumulateInterest(BigDecimal dailyInterest, int days) {
        return quantize(dailyInterest.multiply(BigDecimal.valueOf(days)));
    }

    public static InterestResult calculateInterest(
            BigDecimal principal, BigDecimal annualRate, int days) {
        BigDecimal dailyRate = calcDailyRate(annualRate);
        BigDecimal dailyInterest = calcDailyInterest(principal, dailyRate);
        BigDecimal totalInterest = accumulateInterest(dailyInterest, days);
        BigDecimal newBalance = quantize(principal.add(totalInterest));
        return new InterestResult(
                principal,
                annualRate,
                days,
                dailyRate,
                dailyInterest,
                totalInterest,
                newBalance);
    }

    public static InterestResult calculateInterest(BigDecimal principal) {
        return calculateInterest(principal, DEFAULT_ANNUAL_RATE, 31);
    }

    public static String formatCurrency(BigDecimal amount) {
        return NumberFormat.getCurrencyInstance(Locale.US).format(amount);
    }

    public static void main(String[] args) {
        InterestResult result = calculateInterest(new BigDecimal("12500.50"));

        System.out.println("INTCALC START");
        System.out.println("PRINCIPAL=" + result.principal());
        System.out.println("RATE=" + result.annualRate());
        System.out.println("DAYS=" + result.days());
        System.out.println("DAILY RATE=" + result.dailyRate());
        System.out.println("DAILY INT=" + result.dailyInterest());
        System.out.println("INTEREST=" + result.totalInterest());
        System.out.println("NEW BALANCE=" + formatCurrency(result.newBalance()));
        System.out.println("INTCALC END");
    }
}
