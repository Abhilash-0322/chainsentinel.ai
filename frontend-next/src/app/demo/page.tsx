import { DemoSection } from '@/components/landing/DemoSection';
import { Footer } from '@/components/landing/CTA';

export const metadata = {
    title: 'Demo | Aptos Shield',
    description: 'Try the vulnerability scanner on demo contracts',
};

export default function DemoPage() {
    return (
        <div className="min-h-screen pt-20">
            <DemoSection />
            <Footer />
        </div>
    );
}
