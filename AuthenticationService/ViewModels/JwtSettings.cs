﻿namespace AuthenticationService;

public class JwtSettings
{
    public string SecretKey { get; set; } = string.Empty;
    public string Issuer { get; set; } = string.Empty;
    public string Audience { get; set; } = string.Empty;
    public int TokenExpirationMinutes { get; set; } = 3600;
    public int RefreshTokenExpirationDays { get; set; } = 7;
}