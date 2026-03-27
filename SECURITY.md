# Security Policy

## Responsible Disclosure

If you discover a security vulnerability in vikrant-OBLITERATUS, please report it to:

📧 **vikrantranahome@gmail.com**

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Security Considerations

### Abliteration Tools

1. **Model Provenance**: Always verify model source before abliteration
2. **Dark Web Scanner**: Use `vobl scan` to detect adversarial modifications
3. **Collaboration Sessions**: WebSocket auth via session tokens

### Threat Model

**Dark Web Scanner** detects:
- Poison vectors in model weights
- Adversarial fine-tuning signatures
- Backdoor triggers
- Malicious LoRA adapters

## Supported Versions

| Version | Supported |
|---------|----------|
| 2.x     | ✅       |
| 1.x     | ❌       |

## Security Updates

Security patches are released as needed. Subscribe to [GitHub Releases](https://github.com/vikrantproject/vikrant-OBLITERATUS/releases).
