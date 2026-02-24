# Numeric Limits

| Type                     |       Size*        |                       Range (commonly)                       | Format Specifier |
| :----------------------- | :----------------: | :----------------------------------------------------------: | :--------------: |
| `short int`              |    __2 bytes__     |                    $-32,768 \rarr 32,767$                    |      `%hd`       |
| `unsigned int`           |    __4 bytes__     |                    $0 \rarr 4,294,967,295$                    |       `%u`       |
| `long int`               |      8 bytes       | $-9,223,372,036,854,775,808 \rarr 9,223,372,036,854,775,807$ |      `%ld`       |
| `long long int`          |      8 bytes       | $-9,223,372,036,854,775,808 \rarr 9,223,372,036,854,775,807$ |      `%lld`      |
| `unsigned long long int` |      8 bytes       |             $0 \rarr 18,446,744,073,709,551,615$             |      `%llu`      |
| `long double`            | 8, 12, or 16 bytes | Implementation-dependent, but more precision than __double__ |      `%Lf`       |

