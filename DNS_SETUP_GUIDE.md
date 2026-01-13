# 🌐 DNS Configuration Guide

## Problem: DNS_PROBE_FINISHED_NXDOMAIN

এই error মানে `www.shaznuz.com`-এর DNS record properly configure করা হয়নি।

## ✅ Solution: DNS Records Setup

### Step 1: Vercel এ Domain Add করুন

1. **Vercel Dashboard** এ যান: https://vercel.com/dashboard
2. আপনার project select করুন
3. **Settings** → **Domains** এ যান
4. **Add Domain** button click করুন
5. **Add both domains**:
   - `shaznuz.com` (primary)
   - `www.shaznuz.com` (www subdomain)

### Step 2: Domain Provider এ DNS Records Add করুন

আপনার domain provider (যেমন: Namecheap, GoDaddy, Cloudflare, etc.) এ যান এবং এই DNS records add করুন:

#### Option 1: Vercel Nameservers (Recommended - Easiest)

1. Vercel Dashboard → Domains → আপনার domain → **Nameservers** section
2. Vercel-এর nameservers copy করুন (সাধারণত):
   ```
   ns1.vercel-dns.com
   ns2.vercel-dns.com
   ```
3. আপনার domain provider এ যান
4. Nameservers change করুন Vercel-এর nameservers দিয়ে
5. 24-48 hours wait করুন propagation এর জন্য

#### Option 2: Manual DNS Records (If you want to keep your current nameservers)

আপনার domain provider এ এই DNS records add করুন:

**For shaznuz.com (Root Domain):**
```
Type: A
Name: @
Value: 76.76.21.21
TTL: 3600 (or Auto)
```

**For www.shaznuz.com (WWW Subdomain):**
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
TTL: 3600 (or Auto)
```

**Alternative for www (if CNAME doesn't work):**
```
Type: A
Name: www
Value: 76.76.21.21
TTL: 3600 (or Auto)
```

### Step 3: Verify DNS Configuration

1. **DNS Checker** ব্যবহার করুন:
   - https://dnschecker.org
   - `shaznuz.com` এবং `www.shaznuz.com` check করুন

2. **Command Line** থেকে check করুন:
   ```bash
   # Windows PowerShell
   nslookup shaznuz.com
   nslookup www.shaznuz.com
   
   # Or use online tools
   ```

### Step 4: Wait for DNS Propagation

- DNS changes propagate হতে **24-48 hours** সময় লাগতে পারে
- কিছু cases এ **few minutes** এ কাজ করতে পারে
- Propagation status check করতে: https://dnschecker.org

## 🔍 Troubleshooting

### যদি এখনও কাজ না করে:

1. **Vercel Dashboard Check**:
   - Settings → Domains
   - দেখুন domain properly configured আছে কিনা
   - SSL certificate status check করুন

2. **DNS Records Double Check**:
   - Domain provider এ DNS records correctly added আছে কিনা verify করুন
   - Typo check করুন

3. **Clear DNS Cache**:
   ```bash
   # Windows
   ipconfig /flushdns
   
   # Or restart your router
   ```

4. **Check Domain Status**:
   - Domain expired হয়নি কিনা check করুন
   - Domain properly registered আছে কিনা verify করুন

## 📝 Important Notes

- **Vercel Nameservers** use করলে সব DNS management Vercel handle করবে (easiest option)
- **Manual DNS Records** use করলে আপনাকে manually manage করতে হবে
- DNS propagation সময় লাগতে পারে - patience রাখুন
- SSL certificate automatically issue হবে Vercel থেকে (few minutes)

## ✅ Success Indicators

DNS properly configured হলে:
- ✅ `shaznuz.com` কাজ করবে
- ✅ `www.shaznuz.com` কাজ করবে (redirect হবে `shaznuz.com` এ)
- ✅ SSL certificate automatically active হবে
- ✅ No DNS errors

---

**Need Help?** Vercel Support: https://vercel.com/support
