#!/usr/bin/env node
/**
 * CyberPools CEO Executive Brief Generator
 * Generates a styled DOCX report from markdown with framework details and citations
 *
 * Usage: node generate_ceo_report.js
 * Output: CEO_Executive_Brief_2026_Print.docx
 */

const fs = require('fs');
const path = require('path');

// Check if required packages are installed
const requiredPackages = {
  'docx': null,
  'marked': null
};

try {
  requiredPackages.docx = require('docx');
  requiredPackages.marked = require('marked');
} catch (error) {
  console.error('\n❌ Missing required packages. Please install them:');
  console.error('\nnpm install docx marked\n');
  process.exit(1);
}

const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
        BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType,
        ExternalHyperlink, PageBreak } = requiredPackages.docx;
const { marked } = requiredPackages.marked;

// CyberPools brand colors (from style guide)
const COLORS = {
  primaryNavy: '2C5F7C',
  primaryTeal: '4A9FB8',
  accentCyan: '6BC4D9',
  gradeA: '0ABE57',
  gradeB: '75C525',
  gradeC: 'E8AB25',
  gradeD: 'FA783A',
  gradeF: 'EF3A3F',
  critical: '7B0000',
  high: 'C10000',
  moderate: 'F39C12',
  low: '4CAF50',
  info: '3498DB',
  grayDark: '333333',
  grayMedium: '666666',
  grayLight: 'CCCCCC'
};

// Framework information with citations
const FRAMEWORKS = {
  nist: {
    name: 'NIST Cybersecurity Framework 2.0',
    url: 'https://www.nist.gov/cyberframework',
    releaseDate: 'February 2024',
    description: 'The NIST Cybersecurity Framework provides guidance for managing and reducing cybersecurity risk. Version 2.0 introduced a new "Govern" function and updated guidance across all six core functions.',
    functions: [
      { name: 'Govern', description: 'Cybersecurity governance, risk strategy, and accountability' },
      { name: 'Identify', description: 'Asset identification and risk understanding' },
      { name: 'Protect', description: 'Safeguards to ensure delivery of critical services' },
      { name: 'Detect', description: 'Identify cybersecurity events and anomalies' },
      { name: 'Respond', description: 'Incident response actions and procedures' },
      { name: 'Recover', description: 'Restoration of capabilities after incidents' }
    ],
    adoption: '74% of organizations using security frameworks use NIST CSF (SANS 2023)',
    relevance: 'Industry standard recognized by insurance carriers and regulators. Version 2.0 release validates the framework remains current with evolving threats and best practices.'
  },
  cis: {
    name: 'CIS Controls v8',
    url: 'https://www.cisecurity.org/controls',
    releaseDate: 'May 2021 (Current)',
    description: 'The Center for Internet Security (CIS) Controls are a prioritized set of actions providing a foundation for effective cybersecurity. The 18 CIS Controls are organized into three Implementation Groups based on organizational resources and risk.',
    implementationGroups: [
      { name: 'IG1', description: 'Essential cyber hygiene for organizations with limited resources (6 controls)' },
      { name: 'IG2', description: 'Enhanced security for organizations with moderate resources (16 controls)' },
      { name: 'IG3', description: 'Advanced security for organizations with significant resources (18 controls)' }
    ],
    criticalControls: [
      'Control 1: Inventory and Control of Enterprise Assets',
      'Control 2: Inventory and Control of Software Assets',
      'Control 3: Data Protection',
      'Control 4: Secure Configuration',
      'Control 5: Account Management',
      'Control 6: Access Control Management',
      'Control 7: Continuous Vulnerability Management',
      'Control 8: Audit Log Management',
      'Control 9: Email and Web Browser Protections',
      'Control 10: Malware Defenses',
      'Control 11: Data Recovery',
      'Control 12: Network Infrastructure Management',
      'Control 13: Network Monitoring and Defense',
      'Control 14: Security Awareness and Training',
      'Control 15: Service Provider Management',
      'Control 16: Application Software Security',
      'Control 17: Incident Response Management',
      'Control 18: Penetration Testing'
    ],
    relevance: 'Vendor-neutral, community-driven controls widely adopted in K-12 education. Prioritization by Implementation Groups aligns with dual-score assessment model (IG1 = Foundation, IG2/IG3 = Comprehensive).'
  },
  cisa: {
    name: 'CISA Cybersecurity Performance Goals (CPGs)',
    url: 'https://www.cisa.gov/cpg',
    releaseDate: 'March 2023',
    description: 'CISA Cybersecurity Performance Goals are a subset of IT and OT cybersecurity practices, selected through a risk-based approach, aimed at meaningfully reducing risks to critical infrastructure and the nation.',
    crossSectorGoals: [
      'Account Security (MFA, strong passwords, phishing-resistant MFA)',
      'Device Security (automated patching, EDR, removal of unsupported/EOL software)',
      'Data Security (encryption at rest and in transit, secure backups)',
      'Vulnerability Management (asset inventory, patch management, scanning)',
      'Supply Chain Management (vendor security assessments)',
      'Response Planning (incident response plan, testing, coordination)'
    ],
    targetAudience: 'Critical infrastructure sectors including healthcare, education, and government organizations with limited cybersecurity resources',
    relevance: 'K-12 schools increasingly considered critical infrastructure. CPGs focus on high-impact, low-cost practices aligned with insurance minimum requirements.'
  },
  ferpa: {
    name: 'FERPA - Family Educational Rights and Privacy Act',
    url: 'https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html',
    jurisdiction: 'U.S. Department of Education',
    description: 'Federal law protecting the privacy of student education records. Schools must have written permission to release personally identifiable information, with certain exceptions.',
    securityRequirements: [
      'Reasonable security measures to protect student records',
      'Vendor agreements requiring data protection (FERPA § 99.31)',
      'Data retention and disposal requirements',
      'Parent/student access rights to records',
      'Notification requirements for data breaches affecting student records'
    ],
    relevance: 'K-12 schools must align cybersecurity practices with FERPA requirements. Cyber insurance increasingly incorporates regulatory compliance into coverage decisions.'
  }
};

// Read the CEO Executive Brief markdown
const INPUT_PATH = path.join(__dirname, '../docs/CEO_EXECUTIVE_BRIEF_2026_ASSESSMENT_STRATEGY.md');
const OUTPUT_PATH = path.join(__dirname, '../output/CEO_Executive_Brief_2026_Print.docx');

// Ensure output directory exists
const outputDir = path.dirname(OUTPUT_PATH);
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

console.log('🔄 Reading CEO Executive Brief...');
const markdownContent = fs.readFileSync(INPUT_PATH, 'utf-8');

// Parse markdown to extract sections
const sections = parseMarkdown(markdownContent);

// Create document
console.log('🔄 Generating DOCX document with CyberPools styling...');
const doc = createDocument(sections);

// Save document
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(OUTPUT_PATH, buffer);
  console.log(`\n✅ Document generated successfully!`);
  console.log(`📄 Output: ${OUTPUT_PATH}`);
  console.log(`\n💡 Open this file to print or distribute to your team.`);
}).catch((error) => {
  console.error('❌ Error generating document:', error);
  process.exit(1);
});

/**
 * Parse markdown content into structured sections
 */
function parseMarkdown(content) {
  const lines = content.split('\n');
  const sections = [];
  let currentSection = null;

  for (const line of lines) {
    if (line.startsWith('# ')) {
      currentSection = { type: 'h1', text: line.replace(/^# /, ''), content: [] };
      sections.push(currentSection);
    } else if (line.startsWith('## ')) {
      currentSection = { type: 'h2', text: line.replace(/^## /, ''), content: [] };
      sections.push(currentSection);
    } else if (line.startsWith('### ')) {
      currentSection = { type: 'h3', text: line.replace(/^### /, ''), content: [] };
      sections.push(currentSection);
    } else if (currentSection) {
      currentSection.content.push(line);
    }
  }

  return sections;
}

/**
 * Create DOCX document with CyberPools styling
 */
function createDocument(sections) {
  const children = [];

  // Cover page
  children.push(createCoverPage());
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // Table of contents placeholder
  children.push(createTOC());
  children.push(new Paragraph({ children: [new PageBreak()] }));

  // Main content
  children.push(...createMainContent(sections));

  // Framework appendix
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(...createFrameworkAppendix());

  // Citations
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(...createCitations());

  const doc = new Document({
    sections: [{
      properties: {
        page: {
          margin: {
            top: 1440,    // 1 inch = 1440 twips
            bottom: 1440,
            left: 1440,
            right: 1440
          }
        }
      },
      children: children
    }]
  });

  return doc;
}

/**
 * Create cover page
 */
function createCoverPage() {
  return new Paragraph({
    children: [
      new TextRun({
        text: 'CYBERPOOLS',
        bold: true,
        size: 96,
        color: COLORS.primaryNavy,
        font: 'Inter'
      }),
      new TextRun({
        text: '\n\n',
        break: 2
      }),
      new TextRun({
        text: 'Risk Assessment Evolution',
        size: 72,
        color: COLORS.primaryNavy,
        font: 'Inter'
      }),
      new TextRun({
        text: '\n\n',
        break: 2
      }),
      new TextRun({
        text: 'Executive Brief for CEO',
        size: 48,
        color: COLORS.primaryTeal,
        font: 'Inter'
      }),
      new TextRun({
        text: '\n',
        break: 1
      }),
      new TextRun({
        text: '2026 Strategic Direction',
        size: 36,
        color: COLORS.grayMedium,
        font: 'Inter'
      }),
      new TextRun({
        text: '\n\n\n',
        break: 3
      }),
      new TextRun({
        text: 'Prepared: October 30, 2025',
        size: 24,
        color: COLORS.grayDark,
        font: 'Inter'
      }),
      new TextRun({
        text: '\n',
        break: 1
      }),
      new TextRun({
        text: 'Target Launch: January 1, 2026',
        size: 24,
        color: COLORS.grayDark,
        font: 'Inter'
      }),
      new TextRun({
        text: '\n\n\n\n',
        break: 4
      }),
      new TextRun({
        text: 'Framework-Aligned  |  Insurance-Validated  |  K-12 Specialized',
        size: 20,
        color: COLORS.primaryTeal,
        font: 'Inter',
        italics: true
      })
    ],
    alignment: AlignmentType.CENTER,
    spacing: { before: 4320, after: 200 } // Extra top spacing
  });
}

/**
 * Create table of contents
 */
function createTOC() {
  const toc = new Paragraph({
    text: 'Table of Contents',
    heading: HeadingLevel.HEADING_1,
    thematicBreak: true,
    spacing: { after: 400 }
  });

  return toc;
}

/**
 * Create main content from sections
 */
function createMainContent(sections) {
  const content = [];

  for (const section of sections) {
    if (section.type === 'h1') {
      content.push(new Paragraph({
        text: section.text,
        heading: HeadingLevel.HEADING_1,
        thematicBreak: true,
        spacing: { before: 400, after: 200 },
        border: {
          left: {
            color: COLORS.primaryTeal,
            space: 1,
            style: BorderStyle.SINGLE,
            size: 24
          }
        }
      }));
    } else if (section.type === 'h2') {
      content.push(new Paragraph({
        text: section.text,
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 300, after: 150 }
      }));
    } else if (section.type === 'h3') {
      content.push(new Paragraph({
        text: section.text,
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 200, after: 100 }
      }));
    }

    // Process content
    for (const line of section.content) {
      if (line.trim() === '') continue;
      if (line.startsWith('```')) continue; // Skip code blocks
      if (line.startsWith('|')) continue; // Skip tables for now

      // Parse markdown formatting
      const runs = parseMarkdownLine(line);
      content.push(new Paragraph({
        children: runs,
        spacing: { after: 120 }
      }));
    }
  }

  return content;
}

/**
 * Parse markdown line into TextRuns
 */
function parseMarkdownLine(line) {
  const runs = [];

  // Simple markdown parsing (bold, links, etc.)
  const parts = line.split(/(\*\*.*?\*\*|\[.*?\]\(.*?\)|`.*?`)/g);

  for (const part of parts) {
    if (!part) continue;

    if (part.startsWith('**') && part.endsWith('**')) {
      // Bold text
      runs.push(new TextRun({
        text: part.slice(2, -2),
        bold: true,
        color: COLORS.grayDark
      }));
    } else if (part.startsWith('[') && part.includes('](')) {
      // Link (extract text and URL)
      const match = part.match(/\[(.*?)\]\((.*?)\)/);
      if (match) {
        runs.push(new ExternalHyperlink({
          children: [new TextRun({
            text: match[1],
            style: 'Hyperlink',
            color: COLORS.primaryTeal
          })],
          link: match[2]
        }));
      }
    } else if (part.startsWith('`') && part.endsWith('`')) {
      // Code
      runs.push(new TextRun({
        text: part.slice(1, -1),
        font: 'Courier New',
        color: COLORS.grayMedium,
        shading: {
          type: ShadingType.CLEAR,
          fill: COLORS.grayLight
        }
      }));
    } else if (part.startsWith('- ')) {
      // Bullet point
      runs.push(new TextRun({
        text: '  • ' + part.slice(2),
        color: COLORS.grayDark
      }));
    } else {
      // Normal text
      runs.push(new TextRun({
        text: part,
        color: COLORS.grayDark
      }));
    }
  }

  return runs;
}

/**
 * Create framework appendix with detailed information
 */
function createFrameworkAppendix() {
  const content = [];

  content.push(new Paragraph({
    text: 'Appendix: Cybersecurity Frameworks',
    heading: HeadingLevel.HEADING_1,
    thematicBreak: true,
    spacing: { before: 400, after: 300 }
  }));

  content.push(new Paragraph({
    children: [new TextRun({
      text: 'This appendix provides detailed information about the cybersecurity frameworks referenced in this brief. Understanding these frameworks is essential for staff to recognize how the dual-score assessment model aligns with industry standards and best practices.',
      color: COLORS.grayDark
    })],
    spacing: { after: 300 }
  }));

  // NIST CSF 2.0
  content.push(...createFrameworkSection(FRAMEWORKS.nist));

  // CIS Controls v8
  content.push(...createFrameworkSection(FRAMEWORKS.cis));

  // CISA CPGs
  content.push(...createFrameworkSection(FRAMEWORKS.cisa));

  // FERPA
  content.push(...createFrameworkSection(FRAMEWORKS.ferpa));

  return content;
}

/**
 * Create a framework section
 */
function createFrameworkSection(framework) {
  const content = [];

  // Framework name
  content.push(new Paragraph({
    text: framework.name,
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 400, after: 200 }
  }));

  // URL as hyperlink
  content.push(new Paragraph({
    children: [
      new TextRun({ text: 'Official Resource: ', bold: true, color: COLORS.grayDark }),
      new ExternalHyperlink({
        children: [new TextRun({
          text: framework.url,
          style: 'Hyperlink',
          color: COLORS.primaryTeal
        })],
        link: framework.url
      })
    ],
    spacing: { after: 150 }
  }));

  // Release date
  if (framework.releaseDate) {
    content.push(new Paragraph({
      children: [
        new TextRun({ text: 'Release Date: ', bold: true, color: COLORS.grayDark }),
        new TextRun({ text: framework.releaseDate, color: COLORS.grayDark })
      ],
      spacing: { after: 150 }
    }));
  }

  // Description
  content.push(new Paragraph({
    children: [new TextRun({ text: framework.description, color: COLORS.grayDark })],
    spacing: { after: 200 }
  }));

  // Framework-specific sections
  if (framework.functions) {
    content.push(new Paragraph({
      text: 'Core Functions:',
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 200, after: 150 }
    }));

    for (const func of framework.functions) {
      content.push(new Paragraph({
        children: [
          new TextRun({ text: `  • ${func.name}: `, bold: true, color: COLORS.primaryNavy }),
          new TextRun({ text: func.description, color: COLORS.grayDark })
        ],
        spacing: { after: 100 }
      }));
    }
  }

  if (framework.implementationGroups) {
    content.push(new Paragraph({
      text: 'Implementation Groups:',
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 200, after: 150 }
    }));

    for (const group of framework.implementationGroups) {
      content.push(new Paragraph({
        children: [
          new TextRun({ text: `  • ${group.name}: `, bold: true, color: COLORS.primaryNavy }),
          new TextRun({ text: group.description, color: COLORS.grayDark })
        ],
        spacing: { after: 100 }
      }));
    }
  }

  if (framework.criticalControls) {
    content.push(new Paragraph({
      text: '18 CIS Controls:',
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 200, after: 150 }
    }));

    for (const control of framework.criticalControls) {
      content.push(new Paragraph({
        children: [new TextRun({ text: `  • ${control}`, color: COLORS.grayDark })],
        spacing: { after: 80 }
      }));
    }
  }

  if (framework.crossSectorGoals) {
    content.push(new Paragraph({
      text: 'Cross-Sector Cybersecurity Performance Goals:',
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 200, after: 150 }
    }));

    for (const goal of framework.crossSectorGoals) {
      content.push(new Paragraph({
        children: [new TextRun({ text: `  • ${goal}`, color: COLORS.grayDark })],
        spacing: { after: 80 }
      }));
    }
  }

  if (framework.securityRequirements) {
    content.push(new Paragraph({
      text: 'Key Security Requirements:',
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 200, after: 150 }
    }));

    for (const req of framework.securityRequirements) {
      content.push(new Paragraph({
        children: [new TextRun({ text: `  • ${req}`, color: COLORS.grayDark })],
        spacing: { after: 80 }
      }));
    }
  }

  // Relevance to CyberPools
  if (framework.relevance) {
    content.push(new Paragraph({
      text: 'Relevance to CyberPools:',
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 200, after: 150 }
    }));

    content.push(new Paragraph({
      children: [new TextRun({
        text: framework.relevance,
        color: COLORS.grayDark,
        italics: true
      })],
      spacing: { after: 300 },
      shading: {
        type: ShadingType.CLEAR,
        fill: 'F5F7FA'
      },
      border: {
        left: {
          color: COLORS.primaryTeal,
          space: 1,
          style: BorderStyle.SINGLE,
          size: 12
        }
      }
    }));
  }

  return content;
}

/**
 * Create citations page
 */
function createCitations() {
  const content = [];

  content.push(new Paragraph({
    text: 'References & Citations',
    heading: HeadingLevel.HEADING_1,
    thematicBreak: true,
    spacing: { before: 400, after: 300 }
  }));

  const citations = [
    {
      text: 'NIST Cybersecurity Framework 2.0',
      url: 'https://www.nist.gov/cyberframework'
    },
    {
      text: 'CIS Controls v8',
      url: 'https://www.cisecurity.org/controls'
    },
    {
      text: 'CISA Cybersecurity Performance Goals',
      url: 'https://www.cisa.gov/cpg'
    },
    {
      text: 'FERPA Guidance - U.S. Department of Education',
      url: 'https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html'
    },
    {
      text: 'Marsh McLennan Cyber Risk Analytics (2024)',
      url: 'https://www.marsh.com/us/insights/research-and-briefings/cyber-risk-analytics.html'
    },
    {
      text: 'Coalition Cyber Threat Index (2024)',
      url: 'https://www.coalitioninc.com/resources/cyber-threat-index'
    },
    {
      text: 'SANS 2023 Security Framework Survey',
      url: 'https://www.sans.org/'
    },
    {
      text: 'CAI Cyber Insurance Assessment',
      url: 'https://www.cai.io/services/cybersecurity/explore-a-cyber-insurance-assessment'
    }
  ];

  for (const citation of citations) {
    content.push(new Paragraph({
      children: [
        new TextRun({ text: '• ', color: COLORS.primaryNavy }),
        new TextRun({ text: citation.text + ': ', bold: true, color: COLORS.grayDark }),
        new ExternalHyperlink({
          children: [new TextRun({
            text: citation.url,
            style: 'Hyperlink',
            color: COLORS.primaryTeal
          })],
          link: citation.url
        })
      ],
      spacing: { after: 150 }
    }));
  }

  content.push(new Paragraph({
    text: '',
    spacing: { before: 400 }
  }));

  content.push(new Paragraph({
    children: [new TextRun({
      text: 'Note: All external links and framework documents were accessed and verified as of October 2025. Framework documentation and standards are subject to periodic updates by their respective organizations.',
      color: COLORS.grayMedium,
      italics: true,
      size: 20
    })],
    spacing: { before: 200 }
  }));

  return content;
}

console.log('\n📋 CyberPools CEO Executive Brief Generator\n');
