import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Career Gospel Podcast - Strategic Audit",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #6A1B9A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: black;
        text-align: center;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-left: 4px solid #6A1B9A;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .action-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-left: 4px solid #ffc107;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1.5rem;
        border-left: 4px solid #28a745;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .risk-box {
        background-color: #f8d7da;
        padding: 1.5rem;
        border-left: 4px solid #dc3545;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📊 Navigation")
section = st.sidebar.radio(
    "Go to:",
    ["Executive Summary", "Platform Performance", "Critical Issues", 
     "90-Day Action Plan", "KPIs & Targets", "Risk Management", 
     "Audience Insights", "First 7 Days"]
)

# Header
st.markdown('<div class="main-header">🎙️ Strategic Audit & Brand Equity Report</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Career Gospel Podcast | Q4 2025 – Q1 2026</div>', unsafe_allow_html=True)
st.markdown("**Prepared for:** Purple Crayolá by Oluwatosin Adejumo (Social Media Manager)")
st.markdown("**Audit Date:** January 10, 2026")
st.divider()

# ============================================
# SECTION 1: EXECUTIVE SUMMARY
# ============================================
if section == "Executive Summary":
    st.header("I. Executive Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card"><h2>6.2/10</h2><p>Brand Health Score</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card"><h2>31.58%</h2><p>Peak LinkedIn Engagement</p></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card"><h2>0.06%</h2><p>Instagram Link Conversion</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Strategic Positioning")
    st.markdown("""
    The Career Gospel Podcast has carved out a **high-authority niche at the intersection of 
    Kingdom Principles and Global Professionalism.** However, the current digital ecosystem 
    suffers from **"Structural Friction"** across three critical dimensions:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
        <h4>🔍 Discovery ≠ Conversion</h4>
        <p>15,515 Instagram views but only 1 link tap (0.06% conversion)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
        <h4>📉 Momentum Crisis</h4>
        <p>-57.7% Instagram reach decline, -70% YouTube Shorts decline in 30 days</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="insight-box">
        <h4>⚖️ Platform Imbalance</h4>
        <p>LinkedIn (10-31% engagement) gets less effort than Instagram (declining reach)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="action-box">
    <h3>🎯 Strategic Imperative</h3>
    <p><strong>Transition from "Social Media Posting" to a "Conversion-First Content Engine."</strong></p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 2: PLATFORM PERFORMANCE
# ============================================
elif section == "Platform Performance":
    st.header("II. Platform Performance Overview")
    
    # Platform health scores
    platform_data = {
        'Platform': ['LinkedIn', 'Instagram', 'YouTube', 'WhatsApp'],
        'Health Score': [7.5, 5.5, 4.0, 3.0],
        'Strategic Priority': ['Primary growth lever', 'Discovery channel', 'High potential', 'Critical dependency']
    }
    
    df_platforms = pd.DataFrame(platform_data)
    
    # Create gauge charts
    col1, col2, col3, col4 = st.columns(4)
    
    for idx, (col, platform) in enumerate(zip([col1, col2, col3, col4], df_platforms['Platform'])):
        with col:
            score = df_platforms.loc[idx, 'Health Score']
            
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': platform, 'font': {'size': 16}},
                gauge = {
                    'axis': {'range': [None, 10]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 4], 'color': "#ffcccc"},
                        {'range': [4, 7], 'color': "#ffffcc"},
                        {'range': [7, 10], 'color': "#ccffcc"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': score
                    }
                }
            ))
            
            fig.update_layout(height=250, margin=dict(l=10, r=10, t=50, b=10))
            st.plotly_chart(fig, use_container_width=True)
            st.caption(df_platforms.loc[idx, 'Strategic Priority'])
    
    st.markdown("---")
    
    # Platform performance table
    st.subheader("Platform Performance Matrix")
    
    performance_data = {
        'Channel': ['LinkedIn', 'Instagram', 'YouTube', 'WhatsApp'],
        'Current Performance': [
            '31.58% peak ER, 10.2% avg\n37 followers',
            '69 followers\n0.06% conversion\n-57.7% reach decline',
            '2.4% CTR\n5:13 AVD\n50% drop at 30s',
            '50% of YouTube traffic'
        ],
        'Health Score': ['7.5/10', '5.5/10', '4/10', '3/10'],
        'Strategic Priority': [
            '**Primary growth lever**',
            'Discovery channel (fix conversion)',
            'High potential (fix packaging)',
            'Critical dependency risk'
        ]
    }
    
    df_performance = pd.DataFrame(performance_data)
    st.dataframe(df_performance, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # 30-Day Metrics
    st.subheader("Key Metrics (30-Day Snapshot)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Instagram Metrics")
        metrics_ig = {
            'Metric': ['Views', 'Profile Visits', 'Link Taps', 'Saves'],
            'Value': [1662, 88, 1, 2],
            'Change': ['-57.7%', '-43.2%', '0.06% conv', 'Low utility']
        }
        df_ig = pd.DataFrame(metrics_ig)
        st.dataframe(df_ig, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("#### YouTube & LinkedIn Metrics")
        metrics_other = {
            'Metric': ['YouTube Impressions', 'YouTube CTR', 'LinkedIn Top Post', 'LinkedIn Engagement'],
            'Value': [1700, '2.4%', 1220, '10.2% avg, 31.58% peak']
        }
        df_other = pd.DataFrame(metrics_other)
        st.dataframe(df_other, use_container_width=True, hide_index=True)
    
    # Visualization: Platform comparison
    st.markdown("---")
    st.subheader("Engagement Rate Comparison")
    
    engagement_data = {
        'Platform': ['LinkedIn (Peak)', 'LinkedIn (Avg)', 'Industry Avg', 'Instagram'],
        'Engagement Rate': [31.58, 10.2, 6.5, 2.0]
    }
    
    fig = px.bar(
        engagement_data,
        x='Platform',
        y='Engagement Rate',
        color='Engagement Rate',
        color_continuous_scale='purples',
        text='Engagement Rate'
    )
    
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(
        height=400,
        showlegend=False,
        yaxis_title="Engagement Rate (%)",
        xaxis_title=""
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============================================
# SECTION 3: CRITICAL ISSUES
# ============================================
elif section == "Critical Issues":
    st.header("III. Critical Issues (The '5 Cs')")
    
    issue_tab = st.tabs([
        "1️⃣ YouTube CTR Crisis",
        "2️⃣ Retention Gap",
        "3️⃣ Save Rate Crisis",
        "4️⃣ Conversion Leak",
        "5️⃣ LinkedIn Under-Optimization"
    ])
    
    # Issue 1: YouTube CTR
    with issue_tab[0]:
        st.subheader("YouTube Packaging Crisis (CTR: 2.4%)")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class="risk-box">
            <h4>❌ Problem</h4>
            <p>1,659 of 1,700 impressions result in zero engagement.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Root Cause:**")
            st.markdown("""
            - Generic thumbnails (no emotional triggers)
            - "Episode #X" titles (no discoverability)
            - No A/B testing
            """)
        
        with col2:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Fix</h4>
            <ul>
            <li>Redesign thumbnails: Emotion-led faces, bold text, questions</li>
            <li>Rewrite titles: "How to Navigate Career Burnout as a Christian | Guest Name"</li>
            <li>Deploy TubeBuddy for A/B testing</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Target (30 days)", "3.5% CTR", "+1.1%")
            st.caption("60-68 clicks vs. current 41")
        
        # CTR visualization
        st.markdown("---")
        ctr_data = {
            'Scenario': ['Current', 'Target (30d)', 'Industry Standard'],
            'CTR': [2.4, 3.5, 6.0]
        }
        
        fig = go.Figure(data=[
            go.Bar(x=ctr_data['Scenario'], y=ctr_data['CTR'], 
                   marker_color=['#dc3545', '#ffc107', '#28a745'],
                   text=ctr_data['CTR'],
                   texttemplate='%{text}%',
                   textposition='outside')
        ])
        
        fig.update_layout(
            title="YouTube CTR: Current vs Target vs Industry",
            yaxis_title="Click-Through Rate (%)",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Issue 2: Retention
    with issue_tab[1]:
        st.subheader("YouTube Retention Gap (50% Drop at 30 Seconds)")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class="risk-box">
            <h4>❌ Problem</h4>
            <p>Half the audience leaves before understanding value.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Root Cause:**")
            st.markdown("""
            - Traditional intro delays value delivery
            - No hook in first 30 seconds
            """)
        
        with col2:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Fix</h4>
            <ul>
            <li><strong>Value-First Cold Open:</strong> Start with 15-second compelling clip</li>
            <li><strong>Restructure:</strong> 0:00-0:15 hook, 0:15-0:30 credibility, 0:30-0:60 roadmap</li>
            <li>Add visual pattern interrupts every 30 seconds</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Target (60 days)", "58% retention", "+8%")
        
        # Retention visualization
        st.markdown("---")
        retention_data = {
            'Time (seconds)': [0, 15, 30, 45, 60, 120, 180, 240, 313],
            'Current Retention': [100, 75, 50, 40, 35, 30, 28, 25, 20],
            'Target Retention': [100, 85, 58, 50, 45, 40, 38, 35, 30]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=retention_data['Time (seconds)'], 
                                 y=retention_data['Current Retention'],
                                 mode='lines+markers',
                                 name='Current',
                                 line=dict(color='#dc3545', width=3)))
        fig.add_trace(go.Scatter(x=retention_data['Time (seconds)'], 
                                 y=retention_data['Target Retention'],
                                 mode='lines+markers',
                                 name='Target',
                                 line=dict(color='#28a745', width=3, dash='dash')))
        
        fig.update_layout(
            title="Viewer Retention: Current vs Target",
            xaxis_title="Time (seconds)",
            yaxis_title="Retention (%)",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Issue 3: Save Rate
    with issue_tab[2]:
        st.subheader("Instagram Save Rate Crisis (2 Saves)")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class="risk-box">
            <h4>❌ Problem</h4>
            <p>2 saves against 200+ likes = 1:100 ratio (should be 1:10)</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Root Cause:**")
            st.markdown("""
            - Content is inspirational (transient) not instructional (permanent)
            - Nothing screenshot-worthy or reference-worthy
            """)
        
        with col2:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Fix: Create 4 Framework Posts/Month</h4>
            <ol>
            <li>"5 Scripture-Based Negotiation Tactics" (carousel)</li>
            <li>"The 3-2-1 Framework for Career Decisions"</li>
            <li>"Career Transition Checklist for Christians"</li>
            <li>"AI vs. Higher Intelligence: Decision Matrix"</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Target (60 days)", "12 saves/month", "+10")
    
    # Issue 4: Conversion Leak
    with issue_tab[3]:
        st.subheader("Conversion Funnel Leak (0.06% Link CTR)")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class="risk-box">
            <h4>❌ Problem</h4>
            <p>1 link tap from 1,662 views</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Root Cause:**")
            st.markdown("""
            - ✅ **Bio copy is excellent** (outcome-focused, clear value)
            - ❌ **Link infrastructure is broken:** "bit.ly/3Inpt5W and 1 more" creates confusion
            - No lead magnet visible
            - No email capture
            """)
        
        with col2:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Fix (Week 1)</h4>
            <p><strong>Deploy Beacons/Linktree with:</strong></p>
            <ul>
            <li>🎧 Spotify</li>
            <li>🎥 YouTube</li>
            <li>📧 Newsletter signup</li>
            <li>📄 Free Framework download</li>
            <li>💼 LinkedIn Page</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Target (30 days)", "8 taps/month", "+7")
        
        st.markdown("---")
        st.markdown("**Updated Instagram Bio:**")
        st.code("""
🎙️ Real stories. Real faith at work.
✨ Raising the Global 1% to Lead with Higher Intelligence in the Marketplace
⬇️ Listen, Watch, or Get the Free Framework
🔗 [Beacons link]
        """)
    
    # Issue 5: LinkedIn
    with issue_tab[4]:
        st.subheader("LinkedIn Under-Optimization")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class="risk-box">
            <h4>❌ Problem</h4>
            <p>Highest-performing platform (31% peak engagement) gets lowest effort</p>
            <p><strong>Current:</strong> ~3 posts/month vs. Instagram's 12-15</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Fix</h4>
            <ul>
            <li>Flip ratio: 60% LinkedIn, 40% Instagram</li>
            <li>Target: 10 LinkedIn posts/month</li>
            <li>Launch bi-weekly newsletter</li>
            <li>Use LinkedIn-native formats: PDF carousels, articles, polls</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric("Target (60 days)", "2,500 impressions/post", "+1,280")

# ============================================
# SECTION 4: 90-DAY ACTION PLAN
# ============================================
elif section == "90-Day Action Plan":
    st.header("IV. 90-Day Action Plan")
    
    month_tab = st.tabs(["Month 1: Stop the Bleeding", "Month 2: Rebuild Momentum", "Month 3: Scale What Works"])
    
    # Month 1
    with month_tab[0]:
        st.subheader("Month 1: Stop the Bleeding")
        
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        
        for week in weeks:
            with st.expander(f"📅 {week}", expanded=(week=='Week 1')):
                if week == 'Week 1':
                    st.markdown("""
                    **Tasks:**
                    - ✅ Redesign 5 YouTube thumbnails
                    - ✅ Rewrite 5 YouTube titles
                    - ✅ Build Beacons landing page
                    - ✅ Update Instagram/LinkedIn bio links
                    """)
                elif week == 'Week 2':
                    st.markdown("""
                    **Tasks:**
                    - ✅ A/B test thumbnails (TubeBuddy)
                    - ✅ Create 1st framework post
                    - ✅ Add UTM tracking
                    """)
                elif week == 'Week 3':
                    st.markdown("""
                    **Tasks:**
                    - ✅ Launch LinkedIn Newsletter
                    - ✅ Create lead magnet PDF
                    - ✅ Set up ConvertKit/Mailchimp
                    """)
                elif week == 'Week 4':
                    st.markdown("""
                    **Tasks:**
                    - ✅ Publish newsletter #2
                    - ✅ Create 2nd framework post
                    - ✅ Review analytics
                    """)
        
        st.markdown("---")
        st.subheader("Month 1 Targets")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("YouTube CTR", "3.2%", "+0.8%")
        with col2:
            st.metric("Link Taps", "6-8", "+5-7")
        with col3:
            st.metric("Saves", "6", "+4")
        with col4:
            st.metric("Newsletter", "25-30", "New")
    
    # Month 2
    with month_tab[1]:
        st.subheader("Month 2: Rebuild Momentum")
        
        st.markdown("**Week 5-8 Focus:**")
        st.markdown("""
        - Re-edit 3 episodes (value-first opens)
        - Publish 3 LinkedIn posts/week
        - Test LinkedIn carousels
        - Build content repurposing template
        """)
        
        st.markdown("---")
        st.subheader("Month 2 Targets")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("LinkedIn Impressions", "2,200/post", "+980")
        with col2:
            st.metric("YouTube Retention", "56%", "+6%")
        with col3:
            st.metric("Newsletter", "60", "+30")
        with col4:
            st.metric("Instagram Reach", "Stabilized", "0% to +10%")
    
    # Month 3
    with month_tab[2]:
        st.subheader("Month 3: Scale What Works")
        
        st.markdown("**Week 9-12 Focus:**")
        st.markdown("""
        - 3-4 LinkedIn posts/week
        - Launch referral mechanic
        - Create industry-specific content
        - Document learnings
        """)
        
        st.markdown("---")
        st.subheader("Month 3 Targets")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("LinkedIn Impressions", "2,800/post", "+1,580")
        with col2:
            st.metric("YouTube CTR", "3.8%", "+1.4%")
        with col3:
            st.metric("Link Taps", "12/month", "+11")
        with col4:
            st.metric("Newsletter", "100", "+100")
    
    # Gantt chart
    st.markdown("---")
    st.subheader("90-Day Timeline Visualization")
    
    timeline_data = {
        'Task': [
            'YouTube Thumbnails', 'Beacons Setup', 'Newsletter Launch',
            'Framework Posts', 'LinkedIn Posting', 'Retention Optimization',
            'Content Flywheel', 'Referral Mechanic'
        ],
        'Start': [1, 2, 15, 7, 1, 30, 45, 60],
        'Duration': [14, 7, 75, 83, 90, 60, 45, 30],
        'Phase': ['Month 1', 'Month 1', 'Month 1', 'Ongoing', 'Ongoing', 'Month 2', 'Month 2', 'Month 3']
    }
    
    df_timeline = pd.DataFrame(timeline_data)
    df_timeline['End'] = df_timeline['Start'] + df_timeline['Duration']
    
    fig = px.timeline(
        df_timeline,
        x_start='Start',
        x_end='End',
        y='Task',
        color='Phase',
        color_discrete_map={
            'Month 1': '#dc3545',
            'Month 2': '#ffc107',
            'Month 3': '#28a745',
            'Ongoing': '#6A1B9A'
        }
    )
    
    fig.update_layout(
        xaxis_title="Day",
        yaxis_title="",
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============================================
# SECTION 5: KPIs & TARGETS
# ============================================
elif section == "KPIs & Targets":
    st.header("V. Key Performance Indicators")
    
    st.markdown("""
    <div class="action-box">
    <h3>🎯 Primary KPI</h3>
    <h2>YouTube CTR: 2.4% → 3.8% by Day 90</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Secondary KPIs Dashboard")
    
    # Create KPI tracking table
    kpi_data = {
        'Metric': [
            'LinkedIn Impressions',
            'Link Taps',
            'Instagram Saves',
            'Newsletter Subscribers',
            'YouTube Retention'
        ],
        'Current': [1220, 1, 2, 0, '50%'],
        'Month 1 Target': [1800, '6-8', 6, '25-30', '52%'],
        'Month 2 Target': [2200, 10, 9, 60, '56%'],
        'Month 3 Target': [2800, 12, 12, 100, '58%']
    }
    
    df_kpis = pd.DataFrame(kpi_data)
    
    st.dataframe(df_kpis, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Progress visualization
    st.subheader("90-Day Progress Projection")
    
    tab1, tab2, tab3 = st.tabs(["YouTube CTR", "Newsletter Growth", "LinkedIn Impressions"])
    
    with tab1:
        ctr_progress = {
            'Day': [0, 30, 60, 90],
            'CTR (%)': [2.4, 3.2, 3.5, 3.8]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=ctr_progress['Day'],
            y=ctr_progress['CTR (%)'],
            mode='lines+markers',
            line=dict(color='#6A1B9A', width=3),
            marker=dict(size=10)
        ))
        
        fig.add_hline(y=4.0, line_dash="dash", line_color="green", 
                      annotation_text="Industry Min (4%)")
        
        fig.update_layout(
            title="YouTube CTR Improvement Trajectory",
            xaxis_title="Days",
            yaxis_title="CTR (%)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        newsletter_progress = {
            'Day': [0, 30, 60, 90],
            'Subscribers': [0, 28, 60, 100]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=newsletter_progress['Day'],
            y=newsletter_progress['Subscribers'],
            marker_color='#764ba2',
            text=newsletter_progress['Subscribers'],
            textposition='outside'
        ))
        
        fig.update_layout(
            title="Newsletter Subscriber Growth",
            xaxis_title="Days",
            yaxis_title="Subscribers",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        impressions_progress = {
            'Day': [0, 30, 60, 90],
            'Impressions': [1220, 1800, 2200, 2800]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=impressions_progress['Day'],
            y=impressions_progress['Impressions'],
            mode='lines+markers',
            fill='tozeroy',
                        line=dict(color='#667eea', width=3),
            marker=dict(size=10),
            fillcolor='rgba(102, 126, 234, 0.3)'
        ))
        
        fig.update_layout(
            title="LinkedIn Impressions Growth",
            xaxis_title="Days",
            yaxis_title="Impressions per Post",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# ============================================
# SECTION 6: RISK MANAGEMENT
# ============================================
elif section == "Risk Management":
    st.header("VI. Risk Management")
    
    st.markdown("""
    <div class="insight-box">
    <h4>🛡️ Proactive Risk Mitigation Strategy</h4>
    <p>Identified risks with mitigation plans and contingencies to ensure 90-day success.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Risk table
    risk_data = {
        'Risk': [
            'Instagram Continues Declining',
            'YouTube CTR Doesn\'t Improve',
            'WhatsApp Traffic Plateaus',
            'Creator Burnout'
        ],
        'Probability': ['High', 'Medium', 'High', 'Medium'],
        'Impact': ['Medium', 'High', 'Critical', 'Critical'],
        'Mitigation': [
            'Shift to LinkedIn-first strategy',
            'Study 10 competitors, hire designer',
            'Launch referral mechanic',
            'Content flywheel system'
        ],
        'Contingency': [
            'Pause if engagement <2%',
            'Audit full strategy at Day 60',
            'Test small paid ads budget',
            'Reduce to newsletter only'
        ]
    }
    
    df_risks = pd.DataFrame(risk_data)
    
    # Color-code by probability and impact
    st.dataframe(df_risks, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Risk matrix visualization
    st.subheader("Risk Matrix: Probability vs Impact")
    
    risk_matrix_data = {
        'Risk': ['Instagram Decline', 'YouTube CTR', 'WhatsApp Plateau', 'Burnout'],
        'Probability': [0.8, 0.5, 0.8, 0.5],
        'Impact': [0.5, 0.8, 0.9, 0.9],
        'Size': [30, 40, 45, 45]
    }
    
    fig = px.scatter(
        risk_matrix_data,
        x='Probability',
        y='Impact',
        text='Risk',
        size='Size',
        color='Impact',
        color_continuous_scale='Reds',
        size_max=60
    )
    
    fig.update_traces(textposition='top center')
    fig.update_layout(
        xaxis_title="Probability",
        yaxis_title="Impact",
        height=500,
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[0, 1])
    )
    
    # Add quadrant lines
    fig.add_hline(y=0.5, line_dash="dash", line_color="gray")
    fig.add_vline(x=0.5, line_dash="dash", line_color="gray")
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Detailed risk cards
    st.subheader("Detailed Risk Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="risk-box">
        <h4>🔴 Risk 1: Instagram Decline Continues</h4>
        <p><strong>Probability:</strong> High (current -57.7% trend)</p>
        <p><strong>Impact:</strong> Medium</p>
        <p><strong>Mitigation:</strong></p>
        <ul>
        <li>Shift to LinkedIn-first strategy</li>
        <li>Accept Instagram as "discovery channel"</li>
        <li>Monitor engagement weekly</li>
        </ul>
        <p><strong>Contingency:</strong> Pause Instagram posting if engagement drops below 2%, focus entirely on LinkedIn + YouTube</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="risk-box">
        <h4>🟠 Risk 3: Network Exhaustion (WhatsApp)</h4>
        <p><strong>Probability:</strong> High (50% traffic dependency)</p>
        <p><strong>Impact:</strong> Critical (not scalable)</p>
        <p><strong>Mitigation:</strong></p>
        <ul>
        <li>Launch referral mechanic</li>
        <li>Optimize for YouTube search (SEO)</li>
        <li>Diversify traffic sources</li>
        </ul>
        <p><strong>Contingency:</strong> If traffic plateaus, test small paid advertising budget ($100-200) on LinkedIn or YouTube</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="risk-box">
        <h4>🟡 Risk 2: YouTube CTR Doesn't Improve</h4>
        <p><strong>Probability:</strong> Medium (depends on execution)</p>
        <p><strong>Impact:</strong> High</p>
        <p><strong>Mitigation:</strong></p>
        <ul>
        <li>A/B test 3 thumbnail variants per video</li>
        <li>Study 10+ competitor channels</li>
        <li>Hire designer if DIY doesn't convert</li>
        </ul>
        <p><strong>Contingency:</strong> If CTR stays below 3% after 60 days, audit full YouTube strategy (consider rebranding or pivot to Shorts only)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="risk-box">
        <h4>🟠 Risk 4: Content Creation Burnout</h4>
        <p><strong>Probability:</strong> Medium</p>
        <p><strong>Impact:</strong> Critical (inconsistency kills momentum)</p>
        <p><strong>Mitigation:</strong></p>
        <ul>
        <li>Content flywheel (1 pillar → 10+ assets)</li>
        <li>Batch creation: Record 4 episodes in one day</li>
        <li>Use scheduling tools</li>
        </ul>
        <p><strong>Contingency:</strong> If burnout occurs, reduce to 1 podcast/month + LinkedIn newsletter only until systems are sustainable</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# SECTION 7: AUDIENCE INSIGHTS
# ============================================
elif section == "Audience Insights":
    st.header("VII. Audience Insights")
    
    st.markdown("""
    <div class="action-box">
    <h3>🎯 Unique Market Position</h3>
    <p><strong>"The Barbell Demographic"</strong> - A unique audience profile that sets Career Gospel apart from competitors</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Demographic breakdown
    st.subheader("Audience Composition")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Seniority distribution
        seniority_data = {
            'Seniority Level': ['Entry-Level', 'Mid-Career', 'Senior-Level'],
            'Percentage': [32.4, 40.6, 27.0]
        }
        
        fig = go.Figure(data=[
            go.Pie(
                labels=seniority_data['Seniority Level'],
                values=seniority_data['Percentage'],
                hole=0.4,
                marker=dict(colors=['#667eea', '#cccccc', '#764ba2'])
            )
        ])
        
        fig.update_layout(
            title="Audience by Seniority Level",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Strategic Interpretation:**
        - **Entry-level (32.4%):** You're the "Mentor"
        - **Senior-level (27%):** You're the "Peer"
        - **Missing middle:** Opportunity for career progression content
        """)
    
    with col2:
        # Industry distribution
        industry_data = {
            'Industry': ['Financial Services', 'IT/Consulting', 'Engineering', 'Other'],
            'Percentage': [21.6, 18.0, 15.0, 45.4]
        }
        
        fig = px.bar(
            industry_data,
            x='Industry',
            y='Percentage',
            color='Percentage',
            color_continuous_scale='purples',
            text='Percentage'
        )
        
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(
            title="Audience by Industry",
            yaxis_title="Percentage (%)",
            xaxis_title="",
            height=350,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Key Insight:**
        - High-income, competitive industries
        - Value frameworks, data, and ROI
        - Opportunity: Industry-specific content series
        """)
    
    st.markdown("---")
    
    # Content strategy by audience
    st.subheader("Content Strategy by Audience Segment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>🌱 Entry-Level Content</h4>
        <p><strong>Relationship:</strong> You're the Mentor</p>
        <p><strong>Content Examples:</strong></p>
        <ul>
        <li>"How to Land Your First $80K Role with Kingdom Principles"</li>
        <li>"First 90 Days: Career Success Checklist"</li>
        <li>"Entry-Level to Manager: The Journey"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="action-box">
        <h4>🌉 Mid-Career Bridge Content</h4>
        <p><strong>Opportunity:</strong> Fill the Gap</p>
        <p><strong>Content Examples:</strong></p>
        <ul>
        <li>"The 5-Year Plan: From Coordinator to Director"</li>
        <li>"Breaking into Management with Faith"</li>
        <li>"Career Pivot Strategies for Professionals"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Senior-Level Content</h4>
        <p><strong>Relationship:</strong> You're the Peer</p>
        <p><strong>Content Examples:</strong></p>
        <ul>
        <li>"Leading with Spiritual Intelligence in C-Suite"</li>
        <li>"Executive Decision-Making Framework"</li>
        <li>"Mentoring the Next Generation"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Unique moat
    st.subheader("The Spiritual Intelligence Advantage (Unique Moat)")
    
    st.markdown("""
    <div class="insight-box">
    <h4>🏆 Proof Point</h4>
    <p><strong>"AI vs. Higher Intelligence"</strong> content outperformed all standard career advice across platforms.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Strategic Insight:**
        
        Your differentiation is **NOT** career advice (saturated market).
        
        Your differentiation **IS** the fusion of Kingdom principles with global professionalism.
        
        **This is a Blue Ocean Strategy** - no direct competitors at this intersection.
        
        **Competitive Moat:**
        - Career influencers lack spiritual depth
        - Christian content creators lack professional credibility
        - **You occupy the intersection** = defensible market position
        """)
    
    with col2:
        # Competitive positioning diagram
        positioning_data = {
            'Type': ['Career Influencers', 'Christian Creators', 'Career Gospel'],
            'Spiritual Depth': [2, 9, 9],
            'Professional Credibility': [9, 3, 9]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=positioning_data['Professional Credibility'],
            y=positioning_data['Spiritual Depth'],
            mode='markers+text',
            marker=dict(size=[30, 30, 60], color=['#cccccc', '#cccccc', '#6A1B9A']),
            text=positioning_data['Type'],
            textposition='top center'
        ))
        
        fig.update_layout(
            xaxis_title="Professional Credibility",
            yaxis_title="Spiritual Depth",
            height=350,
            xaxis=dict(range=[0, 10]),
            yaxis=dict(range=[0, 10])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Content series recommendation
    st.subheader("Recommended Content Series")
    
    st.markdown("""
    <div class="action-box">
    <h4>📚 "The [Spiritual Principle] Approach to [Career Challenge]"</h4>
    <p><strong>Examples:</strong></p>
    <ul>
    <li><strong>"The Joseph Framework for Career Setbacks"</strong> - Turning adversity into advantage</li>
    <li><strong>"The Daniel Strategy for Workplace Politics"</strong> - Integrity in challenging environments</li>
    <li><strong>"The Esther Approach to Executive Influence"</strong> - Purpose-driven leadership</li>
    <li><strong>"The Nehemiah Blueprint for Project Management"</strong> - Vision + execution with faith</li>
    <li><strong>"The Proverbs 31 Model for Career Excellence"</strong> - Balancing ambition and values</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 8: FIRST 7 DAYS
# ============================================
elif section == "First 7 Days":
    st.header("VIII. First 7 Days Action Plan")
    
    st.markdown("""
    <div class="action-box">
    <h3>⚡ Start Immediately</h3>
    <p>Don't wait for perfect conditions. These 7 days will establish the foundation for your 90-day transformation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Day-by-day breakdown
    days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
    
    for idx, day in enumerate(days, 1):
        with st.expander(f"📅 {day} (Today)" if idx == 1 else f"📅 {day}", expanded=(idx == 1)):
            if idx == 1:
                st.markdown("""
                **Focus:** YouTube Packaging + Landing Page Setup
                
                **Tasks:**
                1. ✅ Watch 10 YouTube videos in your niche, screenshot thumbnails that made you click
                2. ✅ Redesign your last 3 YouTube thumbnails using "emotion-led" format
                3. ✅ Sign up for Beacons or Linktree account
                
                **Expected Outcome:**
                - 3 new thumbnails ready to upload
                - Landing page account created
                
                **Time Required:** 2-3 hours
                """)
                
                st.info("💡 **Pro Tip:** Focus on thumbnails with faces, bold contrasting text, and curiosity gaps. Study what made YOU click.")
            
            elif idx == 2:
                st.markdown("""
                **Focus:** Tools Setup + Title Optimization
                
                **Tasks:**
                1. ✅ Sign up for TubeBuddy or VidIQ (start A/B testing thumbnails)
                2. ✅ Build Beacons/Linktree landing page with 5 options:
                   - 🎧 Spotify
                   - 🎥 YouTube
                   - 📧 Newsletter signup
                   - 📄 Lead Magnet download
                   - 💼 LinkedIn Page
                3. ✅ Rewrite last 5 YouTube video titles (keyword-first format)
                
                **Expected Outcome:**
                - TubeBuddy/VidIQ installed
                - Landing page live with all links
                - 5 optimized titles ready
                
                **Time Required:** 2-3 hours
                """)
            
            elif idx == 3:
                st.markdown("""
                **Focus:** Email Infrastructure + Lead Magnet
                
                **Tasks:**
                1. ✅ Sign up for ConvertKit or Mailchimp (start building email list)
                2. ✅ Create lead magnet outline: "Christian Professional's Career Decision Framework"
                3. ✅ Add UTM parameters to all landing page links
                
                **Expected Outcome:**
                - Email platform account created
                - Lead magnet outline (table of contents + structure)
                - UTM tracking implemented
                
                **Time Required:** 2 hours
                """)
            
            elif idx == 4:
                st.markdown("""
                **Focus:** First Framework Post + Bio Updates
                
                **Tasks:**
                1. ✅ Design first "framework post" (5 Scripture-Based Negotiation Tactics)
                2. ✅ Add lead magnet section to LinkedIn bio
                3. ✅ Update Instagram bio link text to: "Listen, Watch, or Get the Free Framework"
                
                **Expected Outcome:**
                - First framework post designed (carousel format)
                - Both bios updated with new link infrastructure
                
                **Time Required:** 3 hours
                """)
            
            elif idx == 5:
                st.markdown("""
                **Focus:** Newsletter Launch
                
                **Tasks:**
                1. ✅ Launch LinkedIn Newsletter: "Kingdom + Career Insights"
                2. ✅ Write first newsletter issue (publish or schedule)
                3. ✅ Promote newsletter in LinkedIn post + Instagram story
                
                **Expected Outcome:**
                - Newsletter published on LinkedIn
                - First issue sent
                - Promotional posts scheduled
                
                **Time Required:** 2-3 hours
                """)
            
            elif idx == 6:
                st.markdown("""
                **Focus:** Content Repurposing System
                
                **Tasks:**
                1. ✅ Create content repurposing template (1 podcast → 10+ assets)
                2. ✅ Batch-create 3 YouTube Shorts from last episode
                3. ✅ Schedule next week's LinkedIn posts (3 posts)
                
                **Expected Outcome:**
                - Repurposing template documented
                - 3 Shorts created and uploaded
                - Week 2 content scheduled
                
                **Time Required:** 3-4 hours
                """)
            
            elif idx == 7:
                st.markdown("""
                **Focus:** Review & Adjust
                
                **Tasks:**
                1. ✅ Review Week 1 analytics: CTR changes, link taps, profile visits
                2. ✅ Adjust thumbnails/titles based on data
                3. ✅ Plan Week 2 content (2nd framework post, newsletter issue #2)
                
                **Expected Outcome:**
                - Week 1 performance documented
                - Adjustments identified
                - Week 2 planned
                
                **Time Required:** 1-2 hours
                """)
            
            # Progress indicator
            if idx <= 7:
                progress = idx / 7
                st.progress(progress)
                st.caption(f"Week 1 Progress: {int(progress * 100)}%")
    
    st.markdown("---")
    
    # Week 1 checklist
    st.subheader("Week 1 Completion Checklist")
    
    checklist = [
        "YouTube packaging fixed (thumbnails + titles)",
        "Conversion infrastructure built (landing page + email capture)",
        "Link infrastructure fixed (Beacons/Linktree replacing bit.ly)",
        "Owned audience channel launched (LinkedIn Newsletter)",
        "First 'save-worthy' content created (framework post)",
        "Measurement systems established (UTM tracking + analytics baseline)"
    ]
    
    for item in checklist:
        st.checkbox(item, key=f"checklist_{item}")
    
    st.markdown("---")
    
    st.markdown("""
    <div class="success-box">
    <h3>✅ By the end of Week 1, you will have:</h3>
    <ul>
    <li>Fixed your YouTube packaging (thumbnails + titles)</li>
    <li>Built conversion infrastructure (landing page + email capture)</li>
    <li>Fixed link infrastructure (Beacons/Linktree replacing cryptic bit.ly)</li>
    <li>Launched owned audience channel (LinkedIn Newsletter)</li>
    <li>Created first "save-worthy" content (framework post)</li>
    <li>Established measurement systems (UTM tracking + analytics baseline)</li>
    </ul>
    <p><strong>These foundational changes set the stage for sustainable growth over the next 90 days.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Next steps
    st.subheader("After Week 1: What's Next?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Week 2-4**
        - Continue framework posts (1/week)
        - A/B test thumbnails
        - Build lead magnet PDF
        - Publish newsletter #2
        """)
    
    with col2:
        st.markdown("""
        **Month 2**
        - Re-edit episodes (cold opens)
        - Scale LinkedIn to 3 posts/week
        - Test LinkedIn carousels
        - Launch content flywheel
        """)
    
    with col3:
        st.markdown("""
        **Month 3**
        - Increase to 4 LinkedIn posts/week
        - Launch referral mechanic
        - Create industry-specific content
        - Document learnings for Q2
        """)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("**Report prepared by:** Oluwatosin Adejumo (Social Media Manager)")
st.markdown("**Date:** January 10, 2026")
st.markdown("**Next Review:** April 10, 2026 (90-Day Progress Assessment)")